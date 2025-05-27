from datetime import date
from job_tracker.models.company import Company


class Position:
    title: str
    company: Company
    start_date: date
    end_date: date