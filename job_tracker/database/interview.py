

from job_tracker.database.table import Table


class InterviewTable(Table):

    @classmethod
    def _create(cls):
        curs = cls.conn.cursor()

        sql = f"""
        CREATE TABLE interview (
            interview_id VARCHAR(255) PRIMARY KEY,
            person_id VARCHAR(255),
            name VARCHAR(255),
            date DATE
            CONSTRAINT fk_person FOREIGN KEY (person_id) REFERENCES person(person_id)
        )
        """
        curs.execute(sql)