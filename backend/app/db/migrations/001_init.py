from app.db.models import Base

# รองรับ CON-TECH-01, DOM-PDPA-01, IF-HIS-01: สร้าง schema สำหรับ slots, bookings, audit_logs ตาม spec


def upgrade(engine):
    Base.metadata.create_all(bind=engine)
