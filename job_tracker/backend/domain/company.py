from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship

from job_tracker.backend.domain.base_classes import Base
if TYPE_CHECKING:
    from job_tracker.backend.domain.job import Job

class Company(Base):
    __tablename__ = "company"

    name: Mapped[str] = mapped_column(primary_key=True)
    jobs: Mapped[list["Job"]] = relationship(back_populates="company")
