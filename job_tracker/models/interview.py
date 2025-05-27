from job_tracker.models.person import Person
from datetime import date

class Interview:
    interview_id: str
    interviewer: Person
    date: date