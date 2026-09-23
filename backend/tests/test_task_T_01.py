import importlib.util
from pathlib import Path

from sqlalchemy import create_engine, inspect, text


def test_database_schema_has_required_tables_and_columns():
    from app.config import DATABASE_URL
    from app.db.models import Base

    module_path = Path(__file__).resolve().parents[1] / "app" / "db" / "migrations" / "001_init.py"
    spec = importlib.util.spec_from_file_location("migration_001_init", module_path)
    migration_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(migration_module)

    engine = create_engine("sqlite:///:memory:")
    migration_module.upgrade(engine)

    inspector = inspect(engine)
    tables = inspector.get_table_names()

    assert {"slots", "bookings", "audit_logs"}.issubset(set(tables))

    slots_cols = {c["name"] for c in inspector.get_columns("slots")}
    booking_cols = {c["name"] for c in inspector.get_columns("bookings")}
    audit_cols = {c["name"] for c in inspector.get_columns("audit_logs")}

    assert {"id", "slot_date", "start_time", "package_code", "capacity", "remaining"}.issubset(slots_cols)
    assert {"id", "hn", "slot_id", "booking_date", "queue_no", "status", "created_at"}.issubset(booking_cols)
    assert {"id", "actor_id", "action", "hn", "accessed_at"}.issubset(audit_cols)

    with engine.connect() as conn:
        result = conn.execute(text("SELECT name FROM sqlite_master WHERE type='table' AND name='bookings'"))
        assert result.fetchone() is not None

    assert DATABASE_URL is not None
