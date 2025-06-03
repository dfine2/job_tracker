import json
from typing import Any, Generic, Optional, Type, TypeVar
from sqlalchemy import Enum, Float, ForeignKey, String, TEXT, TypeDecorator
from sqlalchemy.orm import composite, DeclarativeBase, Mapped, mapped_column, relationship

from job_tracker.backend.extensions import db


class BaseModel(db.Model):
    __abstract__ = True

    def to_dict(self):
        return {
            column.name: str(getattr(self, column.name))
            for column in self.__table__.columns
        }
