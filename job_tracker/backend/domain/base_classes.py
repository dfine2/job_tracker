from job_tracker.backend.extensions import db


class BaseModel(db.Model):
    __abstract__ = True

    def to_dict(self):
        return {
            column.name: str(getattr(self, column.name))
            for column in self.__table__.columns
        }
