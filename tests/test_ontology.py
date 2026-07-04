"""Test ontology module — Australian courts, statutes, bar rules."""

from ailawfirm_australia.core.ontology import (
    AustralianBarRule,
    AustralianCourt,
    AustralianStatute,
    Jurisdiction,
    MatterType,
)


class TestAustralianCourt:
    def test_federal_courts_exist(self):
        federal = [c for c in AustralianCourt if c.jurisdiction == "federal"]
        assert len(federal) >= 5  # HCA, FCA, FCAFC, FCFCOA, ART

    def test_art_replaces_aat(self):
        """ART must exist — former AAT, transition October 2024."""
        art = AustralianCourt.ART
        assert art.display_name == "Administrative Review Tribunal"
        assert art.level == "tribunal"
        assert art.jurisdiction == "federal"

    def test_state_supreme_courts(self):
        supremes = [c for c in AustralianCourt if c.level == "superior"]
        assert len(supremes) >= 7  # FCA + 6 state/territory supreme

    def test_court_count_minimum(self):
        """At least 15 courts in the enum."""
        assert len(list(AustralianCourt)) >= 15

    def test_nsw_courts(self):
        nsw = [c for c in AustralianCourt if c.jurisdiction == "NSW"]
        assert len(nsw) >= 3  # SC, CA, DC, LC


class TestAustralianStatute:
    def test_statutes_count_minimum(self):
        assert len(list(AustralianStatute)) >= 10

    def test_privacy_act(self):
        pa = AustralianStatute.PRIVACY_ACT_1988
        assert "Privacy Act 1988" in pa.display_name

    def test_my_health_records_act(self):
        mhr = AustralianStatute.MY_HEALTH_RECORDS_ACT_2012
        assert "My Health Records Act 2012" in mhr.display_name
        assert mhr.category == "health"

    def test_aml_acts(self):
        aml = AustralianStatute.AML_CTF_ACT_2006
        aml2 = AustralianStatute.AML_CTF_AMENDMENT_2024
        assert aml.category == "compliance"
        assert "Tranche 2" in aml2.display_name


class TestAustralianBarRule:
    def test_rules_count(self):
        assert len(list(AustralianBarRule)) >= 4

    def test_rule9_confidentiality(self):
        r9 = AustralianBarRule.LPUCSR_R9_CONFIDENTIALITY
        assert "Rule 9" in r9.display_name
        assert r9.category == "confidentiality"

    def test_rule36_publicity(self):
        r36 = AustralianBarRule.LPUCSR_R36_PUBLICITY
        assert "Rule 36" in r36.display_name
        assert r36.category == "publicity"


class TestMatterType:
    def test_matter_types_count(self):
        assert len(list(MatterType)) >= 8


class TestJurisdiction:
    def test_jurisdictions_count(self):
        assert len(list(Jurisdiction)) >= 9  # federal + 8 state/territory
