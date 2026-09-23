import os

# รองรับ CON-TECH-01: ใช้ PostgreSQL ตามมาตรฐานฝ่าย IT โรงพยาบาล
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///:memory:")
