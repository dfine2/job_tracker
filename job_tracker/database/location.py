from job_tracker.database.table import Table


class LocationTable(Table):

    @classmethod
    def _create(cls):
        curs = cls.conn.cursor()

        sql = f"""
        CREATE TABLE location (
            location_id VARCHAR(255) PRIMARY KEY,
            name VARCHAR(255)
        )
        """
        curs.execute(sql)