import json
from job_tracker.backend.extensions import db
from job_tracker.backend.domain.job import (
    Job,
    Company,
)  # Make sure these inherit from db.Model


def insert_if_not_exists(session, model_class, unique_id_field, data_dict):
    existing = (
        session.query(model_class)
        .filter(unique_id_field == data_dict[unique_id_field.key])
        .first()
    )
    if not existing:
        obj = model_class(**data_dict)
        session.add(obj)
        return obj
    return existing


def load_data():

    with open(
        "/Users/davidfine/Documents/Code/job_tracker/job_tracker/data/jobs.json"
    ) as jobs_file:
        jobs = json.load(jobs_file)
        for job in jobs:
            insert_if_not_exists(db.session, Job, Job.id, job)

    with open(
        "/Users/davidfine/Documents/Code/job_tracker/job_tracker/data/companies.json"
    ) as companies_file:
        companies = json.load(companies_file)
        for company in companies:
            insert_if_not_exists(db.session, Company, Company.name, company)

    db.session.commit()


if __name__ == "__main__":
    load_data()
