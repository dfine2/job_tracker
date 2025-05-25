from job_tracker.models.person import Person
from datetime import date

class Interview:
    id: str
    interviewer: Person
    date: date