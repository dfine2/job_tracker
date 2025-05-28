from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from job_tracker.backend.domain.base_classes import Base

class Location(Base):
    __tablename__ = "location"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String)
