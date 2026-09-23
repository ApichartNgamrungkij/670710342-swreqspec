from sqlalchemy import Column, Date, DateTime, Integer, String, Text, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

# รองรับ CON-TECH-01, DOM-PDPA-01, IF-HIS-01: ตาราง booking และ audit log ตรงตามข้อกำหนด
Base = declarative_base()


class Slot(Base):
    __tablename__ = "slots"

    id = Column(Integer, primary_key=True)
    slot_date = Column(Date, nullable=False)
    start_time = Column(String(10), nullable=False)
    package_code = Column(String(50), nullable=False)
    capacity = Column(Integer, nullable=False)
    remaining = Column(Integer, nullable=False)


class Booking(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True)
    hn = Column(String(20), nullable=False)
    slot_id = Column(Integer, ForeignKey("slots.id"), nullable=False)
    booking_date = Column(Date, nullable=False)
    queue_no = Column(String(50), nullable=True)
    status = Column(String(30), nullable=False, default="confirmed")
    created_at = Column(DateTime, nullable=False)

    slot = relationship("Slot")


class AuditLog(Base):
    __tablename__ = "audit_logs"

    id = Column(Integer, primary_key=True)
    actor_id = Column(String(50), nullable=False)
    action = Column(String(100), nullable=False)
    hn = Column(String(20), nullable=False)
    accessed_at = Column(DateTime, nullable=False)
