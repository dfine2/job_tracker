from sqlite3 import Connection

from job_tracker.models.enums import  Source, Status, WorkModel
from job_tracker.models.company import Company
from job_tracker.models.compensation import Compensation
from job_tracker.models.location import Location

class Job:
    job_id: str
    title: str
    company: Company
    compensation: Compensation
    location: Location
    post_url: str
    source: Source

    work_model: WorkModel
    status: Status = Status.NOT_APPLIED
    
    @staticmethod
    def _create_table(conn: Connection):
        curs = conn.cursor()
        source_values = ",".join(f"'{name.value}'" for name in Source)
        work_model_values = ",".join(f"'{name.value}'" for name in WorkModel)
        status_values = ",".join(f"'{name.value}'" for name in Status)

        sql = f"""
        CREATE TABLE job (
            job_id VARCHAR(255) PRIMARY KEY,
            title VARCHAR(255),
            company_id VARCHAR(255),
            compensation_yearly_low DECIMAL(19, 4),
            compensation_yearly_high DECIMAL(19,4),
            post_url VARCHAR(255),
            source TEXT CHECK(source IN ({source_values})),
            work_model TEXT CHECK(work_model IN ({work_model_values})),
            status TEXT CHECK(status IN ({status_values})),
            location_id VARCHAR(255),
            CONSTRAINT fk_company FOREIGN KEY (company_id) REFERENCES company(company_id)
        )
        """
        curs.execute(sql)