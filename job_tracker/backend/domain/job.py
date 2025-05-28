
from dataclasses import dataclass
import enum
from sqlalchemy import Enum, Float, ForeignKey, String
from sqlalchemy.orm import composite, Mapped, mapped_column, relationship


from job_tracker.backend.domain.application import Application
from job_tracker.backend.domain.base_classes import Base
from job_tracker.backend.domain.benefits import Benefits
from job_tracker.backend.domain.company import Company

class WorkModel(enum.Enum):
    ON_SITE = "On-Site"
    REMOTE = "Remote"
    HYBRID = "Hybrid"


class PostingSource(enum.Enum):
    LINKEDIN = "LinkedIn"
    OTHER="Other"

class PayRate(enum.Enum):
    HOURLY = "hourly"
    DAILY = "daily"
    WEEKLY = "weekly"
    MONTHLY = "monthly"
    ANNUALLY = "annually"

@dataclass
class Compensation():
    low: float
    high: float
    rate: PayRate
    
@dataclass
class Posting():
    source: PostingSource
    link: str


class Job(Base):
    __tablename__ = "job"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String)
    work_model: Mapped[WorkModel] = mapped_column(Enum(WorkModel, name="work_model"))

    compensation_low: Mapped[float] = mapped_column(Float)
    compensation_high: Mapped[float] = mapped_column(Float)
    compensation_rate: Mapped[PayRate] = mapped_column(Enum(PayRate, name="compensation_rate"))
    compensation: Mapped[Compensation] = composite(Compensation, compensation_low, compensation_high, compensation_rate)

    company_id: Mapped[str] = mapped_column(ForeignKey("company.id"))
    company: Mapped[Company] = relationship(back_populates="job")

    application: Mapped[Application] = relationship(back_populates="job", uselist=False, cascade="all, delete_orphan")

    posting_source: Mapped[PostingSource] = mapped_column(Enum(PostingSource, name="posting_source"))
    posting_link: Mapped[str] = mapped_column(String)

    benefits: Mapped[Benefits] = relationship(
        back_populates="job",
        uselist=False,
        cascade="all, delete-orphan"
    )
