
from job_tracker.database.table import Table


class CompanyTable(Table):

    @classmethod
    def _create(cls):
        curs = cls.conn.cursor()

        sql = f"""
        CREATE TABLE company (
            company_id VARCHAR(255) PRIMARY KEY,
            name VARCHAR(255),
            website VARCHAR(255)
        )
        """
        curs.execute(sql)