"""Test brain layer — intent classifier, router."""

from ailawfirm_australia.brain.classifier import classify
from ailawfirm_australia.brain.intents import Intent
from ailawfirm_australia.brain.router import process, route


class TestIntentEnum:
    def test_ten_intents(self):
        assert len(list(Intent)) == 10

    def test_all_values_unique(self):
        values = [i.value for i in Intent]
        assert len(values) == len(set(values))


class TestClassifier:
    def test_court_query_intent(self):
        assert classify("look up the federal court") == Intent.COURT_QUERY
        assert classify("what is the supreme court jurisdiction") == Intent.COURT_QUERY
        assert classify("tell me about ART") == Intent.COURT_QUERY

    def test_citation_lookup_intent(self):
        assert classify("validate [2024] FCAFC 100") == Intent.CITATION_LOOKUP
        assert classify("parse AGLC4 citation (2023) 97 ALJR 100") == Intent.CITATION_LOOKUP
        assert classify("check this CLR reference") == Intent.CITATION_LOOKUP

    def test_calendar_add_intent(self):
        assert classify("schedule a hearing on Friday") == Intent.CALENDAR_ADD
        assert classify("add event to calendar") == Intent.CALENDAR_ADD

    def test_calendar_query_intent(self):
        assert classify("what's on tomorrow") == Intent.CALENDAR_QUERY
        assert classify("upcoming hearings") == Intent.CALENDAR_QUERY

    def test_compliance_flag_intent(self):
        assert classify("this might breach confidentiality") == Intent.COMPLIANCE_FLAG
        assert classify("APP 8 cross-border issue") == Intent.COMPLIANCE_FLAG
        assert classify("My Health Record Section 77") == Intent.COMPLIANCE_FLAG
        assert classify("AML Tranche 2 obligation") == Intent.COMPLIANCE_FLAG
        assert classify("Dayal precedent on AI liability") == Intent.COMPLIANCE_FLAG

    def test_drafting_intent(self):
        assert classify("draft a statement of claim") == Intent.DRAFTING_NEED

    def test_deadline_intent(self):
        assert (
            classify("when does the statute of limitations expire on this file")
            == Intent.DEADLINE_CHECK
        )

    def test_matter_update_intent(self):
        assert classify("update the client file") == Intent.MATTER_UPDATE

    def test_unknown_intent(self):
        assert classify("hello how are you today") == Intent.UNKNOWN
        assert classify("random words") == Intent.UNKNOWN


class TestRouter:
    def test_court_to_court_agent(self):
        assert route(Intent.COURT_QUERY) == "court_agent"

    def test_citation_to_citation_agent(self):
        assert route(Intent.CITATION_LOOKUP) == "citation_agent"

    def test_compliance_to_compliance_agent(self):
        assert route(Intent.COMPLIANCE_FLAG) == "compliance_agent"

    def test_calendar_to_calendar_agent(self):
        assert route(Intent.CALENDAR_ADD) == "calendar_agent"
        assert route(Intent.CALENDAR_QUERY) == "calendar_agent"

    def test_unknown(self):
        assert route(Intent.UNKNOWN) == "unknown"

    def test_process_pipeline(self):
        result = process("validate [2024] FCAFC 100")
        assert result["intent"] == "citation_lookup"
        assert result["agent"] == "citation_agent"
