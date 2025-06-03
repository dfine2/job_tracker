import os

from flask import Flask
from flask_cors import CORS


from job_tracker.backend.extensions import db
from job_tracker.backend.routes import init_routes
from job_tracker.backend.orm import load_data


DB_PATH = os.getenv("DB_PATH", "")


def create_app():
    app = Flask(__name__)
    CORS(app, origins=["http://localhost:3000"])
    app.config.update(
        SQLALCHEMY_DATABASE_URI=f"sqlite:///{DB_PATH}",
        DEBUG=True,
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
    )
    db.init_app(app)

    with app.app_context():
        db.create_all()
        load_data()

    init_routes(app)
    return app


if __name__ == "__main__":
    app = create_app()
    # print(app.config["SQLALCHEMY_DATABASE_URI"])

    app.run(port=5001, host="0.0.0.0")
