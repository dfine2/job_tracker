import json
from typing import Any, Generic, Optional, Type, TypeVar
from sqlalchemy import Enum, Float, ForeignKey, String, TEXT, TypeDecorator
from sqlalchemy.orm import composite, DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass

class Serializable:
    def to_dict(self) -> dict:
        return self.__dict__

    @classmethod
    def from_dict(cls, data: dict):
        return cls(*data)
    
class TextType(TypeDecorator,Serializable):
    impl = TEXT

    def __init__(self, cls: Serializable):
        self._cls = cls
        super().__init__()

    def process_bind_param(self, value: Optional[Serializable], dialect) -> Optional[str]:
        if value is None:
            return None
        return json.dumps(value.to_dict())

    def process_result_value(self, value: Optional[str], dialect) -> Optional[Serializable]:
        if value is None:
            return None
        return self._cls.from_dict(json.loads(value))