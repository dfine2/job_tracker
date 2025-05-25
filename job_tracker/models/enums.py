from enum import Enum


class WorkModel(Enum):
    ON_SITE = "On-Site"
    REMOTE = "Remote"
    HYBRID = "Hybrid"

class Source(Enum):
    LINKEDIN = "LinkedIn"

class Status(Enum):
    NOT_APPLIED = "Not Applied"
    APPLIED = "Applied"
    INTERVIEWING = "Interviewing"
    OFFERED = "Offered"
    REJECTED = "Rejected"