from job_tracker.models.enums import  Source, Status, WorkModel
from job_tracker.models.company import Company
from job_tracker.models.compensation import Compensation
from job_tracker.models.location import Location

class Job:
    id: str
    title: str
    company: Company
    compensation: Compensation
    location: Location
    post_url: str
    source: Source

    work_model: WorkModel
    status: Status = Status.NOT_APPLIED
   