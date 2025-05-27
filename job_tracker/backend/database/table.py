from abc import ABC, abstractmethod
from sqlite3 import Connection
from typing import Optional

class Table(ABC):
    _instance: Optional["Table"] =  None
    conn: Connection
    
    """Singleton Interface"""
    def __new__(cls, conn: Connection):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls.conn = conn
            cls._create()
        return cls._instance
    
    @classmethod
    @abstractmethod
    def _create(cls):
        """Create a new table."""

    