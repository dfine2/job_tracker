import datetime
from dataclasses import asdict
import json
import os

from flask import Flask
from flask_cors import CORS
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from job_tracker.backend.domain.job import Job

x = datetime.datetime.now()


DB_PATH = os.getenv("DB_PATH", "")
engine = create_engine(f"sqlite:///{DB_PATH}", echo=True)
session = sessionmaker(engine)()

jobs = session.query(Job)
app = Flask(__name__)
CORS(app, origins=["http://localhost:3000"])


@app.route("/jobs")
def get_jobs():
    return [json.dumps(job.to_dict()) for job in jobs]


if __name__ == '__main__':
    app.run(port=5001,debug=True)
