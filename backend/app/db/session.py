from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.config import DATABASE_URL

# รองรับ CON-TECH-01: ใช้ engine ที่สลับฐานข้อมูลได้ตาม DATABASE_URL
engine = create_engine(DATABASE_URL, future=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, future=True)
