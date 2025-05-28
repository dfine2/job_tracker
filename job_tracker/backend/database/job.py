from job_tracker.database.table import Table
from job_tracker.domain.enums import PostingSource, Status, WorkModel


class JobTable(Table):

    @classmethod
    def _create(cls):
        curs = cls.conn.cursor()
        source_values = ",".join(f"'{name.value}'" for name in PostingSource)
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
            CONSTRAINT fk_location FOREIGN KEY (location_id) REFERENCES location(location_id)
        )
        """
        curs.execute(sql)