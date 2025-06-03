from flask import request
from job_tracker.backend.domain.job import get_all_jobs, update_job_record
def init_routes(app):
    @app.route("/api/jobs", methods=["GET"])
    def list_jobs():
        response = get_all_jobs()
        return response.json
    @app.route("/api/jobs/<int:job_id>", methods=["PUT"])
    def update_job(job_id):
        data = request.get_json()
        return update_job_record(job_id, data)
