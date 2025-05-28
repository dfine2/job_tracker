from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Text, ForeignKey

from job_tracker.backend.domain.base_classes import Base



class Benefits(Base):
    __tablename__ = "benefits"

    id: Mapped[int] = mapped_column(primary_key=True)

    health_insurance: Mapped[bool] = mapped_column(default=False)
    dental_insurance: Mapped[bool] = mapped_column(default=False)
    vision_insurance: Mapped[bool] = mapped_column(default=False)
    retirement_plan: Mapped[bool] = mapped_column(default=False)
    paid_time_off: Mapped[bool] = mapped_column(default=False)
    parental_leave: Mapped[bool] = mapped_column(default=False)
    remote_stipend: Mapped[bool] = mapped_column(default=False)
    professional_development: Mapped[bool] = mapped_column(default=False)
    stock_options: Mapped[bool] = mapped_column(default=False)

    other: Mapped[str] = mapped_column(Text, nullable=True)

    job_id: Mapped[int] = mapped_column(ForeignKey("job.id"), unique=True)
    job = relationship("job", back_populates="benefits")