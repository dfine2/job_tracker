from job_tracker.database.company import CompanyTable
from job_tracker.database.interview import InterviewTable
from job_tracker.database.job import JobTable
from job_tracker.database.location import LocationTable
from job_tracker.database.utils import get_db_conn
def initialize_db():
    conn = get_db_conn()

    JobTable(conn)
    CompanyTable(conn)
    LocationTable(conn)
    InterviewTable(conn)



    
if __name__ == "__main__":
    initialize_db()