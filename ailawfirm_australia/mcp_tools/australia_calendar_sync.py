"""MCP Tool: australia_calendar_sync.

PROVENANCE: CITED:18-life-of-solo-advocate-typical-day.md
"""


def sync_calendar_event(
    title: str,
    start_time: str,
    end_time: str,
    description: str = "",
    timezone: str = "Australia/Sydney",
    output_path: str = None,
) -> dict:
    """Create an ICS calendar event for an Australian legal matter.

    Delegates to calendar_agent.create_calendar_event.
    """
    from ..agents.calendar_agent import create_calendar_event

    return create_calendar_event(
        title=title,
        start_time=start_time,
        end_time=end_time,
        description=description,
        timezone=timezone,
        output_path=output_path,
    )
