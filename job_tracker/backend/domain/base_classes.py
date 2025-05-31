import json
from typing import Any, Generic, Optional, Type, TypeVar
from sqlalchemy import Enum, Float, ForeignKey, String, TEXT, TypeDecorator
from sqlalchemy.orm import composite, DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):

    def to_dict(self):
        return {
            column.name: str(getattr(self, column.name))
            for column in self.__table__.columns
        }
