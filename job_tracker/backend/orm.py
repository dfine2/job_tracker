import json
import os
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker, Session
from job_tracker.backend.domain.base_classes import Base
from job_tracker.backend.domain.job import (
    Job,
    Company,
)

DB_PATH = os.getenv("DB_PATH", "")
engine = create_engine(f"sqlite:///{DB_PATH}", echo=True)


def insert_if_not_exists(session: Session, model_class, unique_id_field, data_dict):
    existing = session.scalar(
        select(model_class).where(unique_id_field == data_dict[unique_id_field.key])
    )
    if not existing:
        obj = model_class(**data_dict)
        session.add(obj)
        return obj
    return existing


Base.metadata.create_all(engine)


session = sessionmaker(bind=engine)()

with open(
    "/Users/davidfine/Documents/Code/job_tracker/job_tracker/data/jobs.json"
) as jobs_file:
    jobs = json.load(jobs_file)

    for job in jobs:
        insert_if_not_exists(session, Job, Job.id, job)

with open(
    "/Users/davidfine/Documents/Code/job_tracker/job_tracker/data/companies.json"
) as companies_file:
    companies = json.load(companies_file)

    for company in companies:
        insert_if_not_exists(session, Company, Company.name, company)

session.commit()
