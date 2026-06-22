"""Intent classification — 10 classes for AI Brain Australia v0.1."""

from enum import Enum


class Intent(Enum):
    MATTER_UPDATE = "matter_update"
    CITATION_LOOKUP = "citation_lookup"
    COURT_QUERY = "court_query"
    DRAFTING_NEED = "drafting_need"  # stub agent in v0.1
    DEADLINE_CHECK = "deadline_check"  # stub agent in v0.1
    CLIENT_COMM = "client_comm"
    COMPLIANCE_FLAG = "compliance_flag"
    CALENDAR_QUERY = "calendar_query"
    CALENDAR_ADD = "calendar_add"
    UNKNOWN = "unknown"
