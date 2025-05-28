import enum

from sqlalchemy import Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship

from job_tracker.backend.domain.base_classes import Base
from job_tracker.backend.domain.job import Job





class ApplicationStatus(enum.Enum):
    NOT_APPLIED = "Not Applied"
    APPLIED = "Applied"
    INTERVIEWING = "Interviewing"
    OFFERED = "Offered"
    REJECTED = "Rejected"

class Application(Base):
    __tablename__ = "application"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    job: Mapped[Job] = relationship(back_populates="application")
    status: Mapped[ApplicationStatus] = mapped_column(Enum(ApplicationStatus, name="status"))