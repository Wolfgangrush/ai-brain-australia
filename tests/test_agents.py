"""Test specialist agents — compliance, court, citation, calendar, stubs."""

from ailawfirm_australia.agents.calendar_agent import (
    AUSTRALIAN_TIMEZONES,
    create_calendar_event,
    list_australian_timezones,
)
from ailawfirm_australia.agents.citation_agent import validate_citation
from ailawfirm_australia.agents.compliance_agent import check_compliance
from ailawfirm_australia.agents.court_agent import get_art_currency_warning, lookup_court
from ailawfirm_australia.agents.deadline_agent import handle_deadline
from ailawfirm_australia.agents.drafting_agent import handle_drafting
from ailawfirm_australia.agents.matter_agent import handle_matter


class TestComplianceAgent:
    def test_clean_input_no_flags(self):
        result = check_compliance("schedule a meeting for tomorrow")
        assert result.all_clear

    def test_rule9_cloud_ai_with_client_data(self):
        result = check_compliance("I uploaded the client case notes to chatgpt for summarization")
        assert not result.all_clear
        assert result.has_critical
        flag_msgs = [f.message.lower() for f in result.flags]
        assert any("rule 9" in m or "lpul" in m for m in flag_msgs)

    def test_app8_cross_border(self):
        result = check_compliance(
            "we should disclose this client personal info to our overseas data processor"
        )
        assert not result.all_clear
        assert result.has_high
        assert any("app 8" in f.message.lower() for f in result.flags)

    def test_section77_health_data_cloud(self):
        result = check_compliance(
            "I want to upload these patient medical records to the cloud API for analysis"
        )
        assert not result.all_clear
        assert result.has_critical
        assert any(
            "section 77" in f.message.lower() or "my health record" in f.message.lower()
            for f in result.flags
        )

    def test_section77_health_data_without_offshore(self):
        result = check_compliance("review these medical records locally")
        assert not result.all_clear  # health data triggers high flag
        assert result.has_high

    def test_aml_tranche2_flag(self):
        result = check_compliance("do we need to do KYC for this client under AML obligations")
        assert not result.all_clear
        assert result.has_high
        assert any(
            "aml" in f.message.lower() or "tranche 2" in f.message.lower() for f in result.flags
        )

    def test_ai_output_without_review(self):
        result = check_compliance("I'm going to file this AI-generated draft without reviewing it")
        assert not result.all_clear
        flag_msgs = [f.message.lower() for f in result.flags]
        assert any("dayal" in m or "human" in m or "review" in m for m in flag_msgs)

    def test_rule36_publicity(self):
        result = check_compliance("I am the best lawyer in Sydney and guarantee your win")
        assert not result.all_clear
        flag_msgs = [f.message.lower() for f in result.flags]
        assert any("rule 36" in m or "publicity" in m for m in flag_msgs)


class TestCourtAgent:
    def test_hca_lookup(self):
        result = lookup_court(court_code="HCA")
        assert result["count"] == 1
        assert result["results"][0]["code"] == "HCA"
        assert "High Court of Australia" in result["results"][0]["name"]

    def test_fca_lookup(self):
        result = lookup_court(court_code="FCA")
        assert result["count"] >= 1
        assert any("Federal Court" in r.get("name", "") for r in result["results"])

    def test_partial_name_lookup(self):
        result = lookup_court(court_name="Supreme")
        assert result["count"] >= 7  # all state/territory supreme courts + HCA

    def test_jurisdiction_filter(self):
        result = lookup_court(jurisdiction="NSW")
        assert result["count"] >= 3
        for r in result["results"]:
            assert r["jurisdiction"] == "NSW"

    def test_art_lookup(self):
        result = lookup_court(court_code="ART")
        assert result["count"] >= 1
        art_result = result["results"][0]
        assert "Administrative Review Tribunal" in art_result["name"]
        assert art_result["level"] == "tribunal"

    def test_art_currency_warning(self):
        warning = get_art_currency_warning()
        assert "October 2024" in warning["transition_date"]
        assert "AAT" in warning["warning"]

    def test_vsc_lookup(self):
        result = lookup_court(court_code="VSC")
        assert result["count"] == 1
        assert "Supreme Court of Victoria" in result["results"][0]["name"]

    def test_qsc_lookup(self):
        result = lookup_court(court_code="QSC")
        assert result["count"] == 1


class TestCitationAgent:
    def test_medium_neutral_valid(self):
        result = validate_citation("[2024] FCAFC 100")
        assert result["valid"]
        assert result["type"] == "medium-neutral"
        assert result["components"]["year"] == 2024
        assert result["components"]["court"] == "FCAFC"
        assert result["components"]["number"] == 100

    def test_reported_citation(self):
        result = validate_citation("(2023) 97 ALJR 100")
        assert result["valid"]
        assert result["type"] == "reported"
        assert result["components"]["volume"] == 97
        assert result["components"]["reporter"].strip() == "ALJR"

    def test_hca_citation(self):
        result = validate_citation("[2023] HCA 12")
        assert result["valid"]
        assert result["components"]["court"] == "HCA"

    def test_nswca_citation(self):
        result = validate_citation("[2023] NSWCA 45")
        assert result["valid"]
        assert result["components"]["court"] == "NSWCA"

    def test_nswsc_citation(self):
        result = validate_citation("[2023] NSWSC 1000")
        assert result["valid"]
        assert result["components"]["court"] == "NSWSC"

    def test_vsc_citation(self):
        result = validate_citation("[2024] VSC 500")
        assert result["valid"]
        assert result["components"]["court"] == "VSC"

    def test_qsc_citation(self):
        result = validate_citation("[2024] QSC 200")
        assert result["valid"]
        assert result["components"]["court"] == "QSC"

    def test_invalid_format(self):
        result = validate_citation("this is not a citation at all")
        assert not result["valid"]
        assert len(result["errors"]) > 0

    def test_canonical_form(self):
        result = validate_citation("[2024] FCAFC 100")
        assert result["canonical"] == "[2024] FCAFC 100"


class TestCalendarAgent:
    def test_create_event_success(self):
        import os
        import tempfile

        tmpdir = tempfile.mkdtemp()
        ics_path = os.path.join(tmpdir, "test.ics")
        result = create_calendar_event(
            title="Directions Hearing — Matter ATY-2024-001",
            start_time="2026-06-15T10:00",
            end_time="2026-06-15T11:00",
            description="Federal Court directions hearing",
            timezone="Australia/Sydney",
            output_path=ics_path,
        )
        assert result["success"]
        assert os.path.exists(ics_path)
        assert result["event"]["timezone"] == "Australia/Sydney"
        os.remove(ics_path)
        os.rmdir(tmpdir)

    def test_create_event_invalid_tz(self):
        result = create_calendar_event(
            title="Test",
            start_time="2026-06-15T10:00",
            end_time="2026-06-15T11:00",
            timezone="America/New_York",
        )
        assert not result["success"]
        assert "Unknown timezone" in result["error"]

    def test_create_event_end_before_start(self):
        result = create_calendar_event(
            title="Test",
            start_time="2026-06-15T11:00",
            end_time="2026-06-15T10:00",
        )
        assert not result["success"]

    def test_list_timezones(self):
        tzs = list_australian_timezones()
        assert len(tzs) == 8
        assert any(tz["name"] == "Australia/Sydney" for tz in tzs)

    def test_brisbane_no_dst(self):
        tzs = list_australian_timezones()
        bne = next(tz for tz in tzs if tz["name"] == "Australia/Brisbane")
        assert not bne["observes_dst"]

    def test_perth_no_dst(self):
        tzs = list_australian_timezones()
        perth = next(tz for tz in tzs if tz["name"] == "Australia/Perth")
        assert not perth["observes_dst"]

    def test_sydney_observes_dst(self):
        tzs = list_australian_timezones()
        syd = next(tz for tz in tzs if tz["name"] == "Australia/Sydney")
        assert syd["observes_dst"]

    def test_ics_valid_rfc5545(self):
        import os
        import tempfile

        from icalendar import Calendar

        tmpdir = tempfile.mkdtemp()
        ics_path = os.path.join(tmpdir, "valid.ics")
        result = create_calendar_event(
            title="Mention — FCA",
            start_time="2026-07-01T09:30",
            end_time="2026-07-01T10:00",
            timezone="Australia/Sydney",
            output_path=ics_path,
        )
        assert result["success"]
        with open(ics_path, "rb") as f:
            cal = Calendar.from_ical(f.read())
        assert cal.get("version") == "2.0"
        event = cal.walk("VEVENT")[0]
        assert "FCA" in str(event.get("summary"))
        os.remove(ics_path)
        os.rmdir(tmpdir)

    def test_all_tz_names(self):
        assert len(AUSTRALIAN_TIMEZONES) == 8
        # Must include the NO-DST ones
        assert "Australia/Brisbane" in AUSTRALIAN_TIMEZONES
        assert "Australia/Perth" in AUSTRALIAN_TIMEZONES
        assert "Australia/Darwin" in AUSTRALIAN_TIMEZONES


class TestStubAgents:
    def test_matter_agent_stub(self):
        result = handle_matter("show my matters")
        assert result["agent"] == "matter_agent"
        assert result["status"] == "stub"

    def test_drafting_agent_stub(self):
        result = handle_drafting("draft a contract")
        assert result["agent"] == "drafting_agent"
        assert result["status"] == "stub"
        assert "compliance_note" in result

    def test_deadline_agent_stub(self):
        result = handle_deadline("what is the limitation period")
        assert result["agent"] == "deadline_agent"
        assert result["status"] == "stub"
        assert "limitation_note" in result
