from job_tracker.database.table import Table


class PersonTable(Table):

    @classmethod
    def _create(cls):
        curs = cls.conn.cursor()

        sql = f"""
        CREATE TABLE person (
            person_id VARCHAR(255) PRIMARY KEY,
            full_name VARCHAR(255),
            first_name VARCHAR(255),
            last_name VARCHAR(255),
            current_position_title

        )
        """
        curs.execute(sql)