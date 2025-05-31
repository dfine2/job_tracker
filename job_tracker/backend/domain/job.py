from dataclasses import dataclass
import enum
from typing import Optional
from sqlalchemy import CheckConstraint, Enum, Float, ForeignKey, String
from sqlalchemy.orm import composite, Mapped, mapped_column, relationship


from job_tracker.backend.domain.base_classes import Base
# from job_tracker.backend.domain.benefits import Benefits
from job_tracker.backend.domain.company import Company

class WorkModel(enum.Enum):
    ON_SITE = "On-Site"
    REMOTE = "Remote"
    HYBRID = "Hybrid"
work_model_contraint = ", ".join(f"'{member.value}'" for member in WorkModel)

class PostingSource(enum.Enum):
    LINKEDIN = "LinkedIn"
    OTHER="Other"
posting_source_contraint = ", ".join(f"'{member.value}'" for member in PostingSource)

@dataclass
class Compensation():
    low: float
    high: float

@dataclass
class Posting():
    source: PostingSource
    link: str


class ApplicationStatus(enum.Enum):
    NOT_APPLIED = "Not Applied"
    APPLIED = "Applied"
    INTERVIEWING = "Interviewing"
    OFFERED = "Offered"
    REJECTED = "Rejected"
application_status_contraint = ", ".join(
    f"'{member.value}'" for member in ApplicationStatus
)


@dataclass
class Application:

    status: ApplicationStatus = ApplicationStatus.NOT_APPLIED

    resume_path: Optional[str] = None
    cover_letter_path: Optional[str] = None


class Job(Base):
    __tablename__ = "job"
    __table_args__ = (
        CheckConstraint(f"work_model IN ({work_model_contraint})"),
        CheckConstraint(f"application_status IN ({application_status_contraint})"),
        CheckConstraint(f"posting_source IN ({posting_source_contraint})"),
    )

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String)
    work_model: Mapped[String] = mapped_column(String)

    compensation_low: Mapped[float] = mapped_column(Float)
    compensation_high: Mapped[float] = mapped_column(Float)
    compensation: Mapped[Compensation] = composite(
        Compensation, compensation_low, compensation_high
    )

    company_name: Mapped[str] = mapped_column(ForeignKey("company.name"))
    company: Mapped[Company] = relationship(back_populates="jobs")

    application_status: Mapped[str] = mapped_column(
        String,
        default=ApplicationStatus.NOT_APPLIED.value,
    )
    application_resume_path: Mapped[Optional[str]] = mapped_column(String, default=None)
    application_cover_letter_path: Mapped[Optional[str]] = mapped_column(
        String, default=None
    )
    application_date: Mapped[Optional[str]] = mapped_column(String, default=None)
    application: Mapped[Application] = composite(
        Application,
        application_status,
        application_resume_path,
        application_cover_letter_path,
    )

    posting_source: Mapped[String] = mapped_column(String)
    posting_link: Mapped[str] = mapped_column(String)
    posting: Mapped[Posting] = composite(Posting, posting_source, posting_link)

    location: Mapped[Optional[str]] = mapped_column(String, nullable=True)
