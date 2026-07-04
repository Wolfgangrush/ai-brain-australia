"""Calendar agent — ICS sync with multi-TZ Australian support.

PROVENANCE: CITED:18-life-of-solo-advocate-typical-day.md (hearing/mention workflow)
"""

from datetime import datetime
from pathlib import Path

from ..config import DEFAULT_CALENDAR_DIR

# Australian timezones — DST-aware via zoneinfo (Python 3.10+)
# PROVENANCE: Sydney default
AUSTRALIAN_TIMEZONES = [
    "Australia/Sydney",  # NSW (DST) — default
    "Australia/Melbourne",  # VIC (DST)
    "Australia/Brisbane",  # QLD (NO DST)
    "Australia/Perth",  # WA (NO DST)
    "Australia/Adelaide",  # SA (DST — ACST)
    "Australia/Hobart",  # TAS (DST)
    "Australia/Darwin",  # NT (NO DST — ACST)
    "Australia/ACT",  # Usually Australia/Sydney — for explicit naming
]

# Note on DST handling:
# zoneinfo handles DST automatically. Sydney/Melbourne/Adelaide/Hobart observe DST.
# Brisbane/Perth/Darwin do NOT observe DST (correct per python zoneinfo).
# Test: create event at 2:30am on DST switchover date and verify offset.


def create_calendar_event(
    title: str,
    start_time: str,
    end_time: str,
    description: str = "",
    timezone: str = "Australia/Sydney",
    output_path: str = None,
) -> dict:
    """Create an ICS calendar event for an Australian legal matter.

    entity-aliasing summary line in event title, full detail in event body.
    Uses icalendar library for RFC 5545 compliance.
    DST handling via zoneinfo (Python 3.10+).

    Args:
        title: Event summary (alias-safe — client codes or matter refs only)
        start_time: ISO 8601 (YYYY-MM-DDTHH:MM)
        end_time: ISO 8601 (YYYY-MM-DDTHH:MM)
        description: Full event description
        timezone: Australia/ timezone (default: Australia/Sydney)
        output_path: .ics file path (default: ~/.ailawfirm-australia/calendars/<slug>.ics)
    """
    from zoneinfo import ZoneInfo

    from icalendar import Calendar, Event

    if timezone not in AUSTRALIAN_TIMEZONES:
        return {
            "success": False,
            "error": f"Unknown timezone: {timezone}. Supported: {AUSTRALIAN_TIMEZONES}",
        }

    try:
        tz = ZoneInfo(timezone)
        dt_start = datetime.fromisoformat(start_time).replace(tzinfo=tz)
        dt_end = datetime.fromisoformat(end_time).replace(tzinfo=tz)
    except ValueError as e:
        return {"success": False, "error": f"Invalid date/time format: {e}"}

    if dt_end <= dt_start:
        return {"success": False, "error": "End time must be after start time"}

    # Build ICS event
    cal = Calendar()
    cal.add("prodid", "-//AI Brain Australia//ailawfirm-australia//EN")
    cal.add("version", "2.0")
    cal.add("calscale", "GREGORIAN")
    cal.add("method", "PUBLISH")
    cal.add("x-wr-calname", "AI Brain — Australia")

    event = Event()
    event.add("summary", title)
    event.add("dtstart", dt_start)
    event.add("dtend", dt_end)
    event.add("dtstamp", datetime.now(tz=tz))
    event.add("uid", f"{dt_start.isoformat()}-{hash(title)}@ailawfirm-australia")

    if description:
        event.add("description", description)

    cal.add_component(event)

    # Determine output path
    if output_path:
        ics_path = Path(output_path)
    else:
        ics_dir = Path(DEFAULT_CALENDAR_DIR)
        ics_dir.mkdir(parents=True, exist_ok=True)
        safe_name = "".join(c if c.isalnum() else "-" for c in title)[:50]
        ics_path = ics_dir / f"{safe_name}-{dt_start.strftime('%Y%m%d')}.ics"

    ics_path.write_bytes(cal.to_ical())

    return {
        "success": True,
        "ics_path": str(ics_path),
        "event": {
            "title": title,
            "start": dt_start.isoformat(),
            "end": dt_end.isoformat(),
            "timezone": timezone,
            "dst_observed": _timezone_observes_dst(timezone),
        },
    }


def list_australian_timezones() -> list[dict]:
    """List supported Australian timezones with DST info."""
    import datetime as dt
    from zoneinfo import ZoneInfo

    result = []
    for tz_name in AUSTRALIAN_TIMEZONES:
        tz = ZoneInfo(tz_name)
        now = dt.datetime.now(tz=tz)
        result.append(
            {
                "name": tz_name,
                "utc_offset": str(now.utcoffset()),
                "observes_dst": _timezone_observes_dst(tz_name),
                "current_time": now.isoformat(),
            }
        )
    return result


def _timezone_observes_dst(tz_name: str) -> bool:
    """Check if a timezone observes DST. Perth + Brisbane + Darwin = NO DST."""
    no_dst = {"Australia/Brisbane", "Australia/Perth", "Australia/Darwin"}
    return tz_name not in no_dst


def handle(payload: str) -> dict:
    """Calendar agent entry point — keyword dispatch to create_calendar_event / list_australian_timezones.

    Routes a free-form payload to the most relevant calendar function. When the
    payload looks like a "list timezones" request, returns the timezone roster.
    Otherwise, extracts title / start / end / timezone hints and calls
    create_calendar_event with safe defaults so the agent always responds.
    Always returns a dict that includes ``"agent": "calendar_agent"``.
    """
    text = (payload or "").strip()
    lower = text.lower()
    if not text:
        return {
            "agent": "calendar_agent",
            "ok": False,
            "error": "empty payload",
            "available_actions": ["create_calendar_event", "list_australian_timezones"],
        }

    list_triggers = (
        "list timezones",
        "list tz",
        "timezones",
        "supported timezones",
        "australian timezones",
    )
    if any(t in lower for t in list_triggers):
        return {
            "agent": "calendar_agent",
            "ok": True,
            "action": "list_australian_timezones",
            "result": list_australian_timezones(),
        }

    # Default: create event with parsed fields and safe defaults.
    title_hint = text[:60]
    timezone_hint = "Australia/Sydney"
    for tz in AUSTRALIAN_TIMEZONES:
        token = tz.split("/")[-1].lower()
        if token in lower:
            timezone_hint = tz
            break

    start_hint = "2026-07-04T09:00"
    end_hint = "2026-07-04T10:00"
    import re

    iso = re.findall(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}", text)
    if iso:
        start_hint = iso[0]
        end_hint = iso[1] if len(iso) > 1 else iso[0]

    event_result = create_calendar_event(
        title=title_hint,
        start_time=start_hint,
        end_time=end_hint,
        description=text,
        timezone=timezone_hint,
    )

    return {
        "agent": "calendar_agent",
        "action": "create_calendar_event",
        "result": event_result,
    }
