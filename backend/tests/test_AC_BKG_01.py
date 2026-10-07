# test ของ T-03: จองคิวสำเร็จ
# AC-BKG-01 (FR-BKG-04)
from app.db.models import Slot
from tests.conftest import AUTH


def test_TC_BKG_01_1_booking_success(client, db, make_slot):
    """TC-BKG-01-1: สำเร็จเมื่อมีที่นั่งว่าง 1 ที่และยืนยันตัวตนแล้ว"""
    # Given: ยืนยันตัวตนแล้ว และช่วง 09.00 น. มีที่นั่งว่าง 1 ที่
    slot = make_slot(start="09:00", remaining=1)

    # When: ผู้ใช้ยืนยันการจองช่วง 09.00 น.
    res = client.post("/bookings", json={"slot_id": slot.id}, headers=AUTH)

    # Then: บันทึกการจองสำเร็จ, แสดงหมายเลขคิว, และที่นั่งว่างของช่วงนั้นเป็น 0
    assert res.status_code == 201
    body = res.json()
    assert "queue_no" in body
    assert body["queue_no"]
    assert body["queue_no"].startswith("A")

    slot_after = db.get(Slot, slot.id)
    assert slot_after.remaining == 0


def test_TC_BKG_01_2_booking_remaining_hits_zero(client, db, make_slot):
    """TC-BKG-01-2: การจองสุดท้ายต้องลดที่นั่งเหลือเป็น 0"""
    # Given: ช่วง 09.00 น. มีที่นั่งว่าง 1 ที่ ก่อนยืนยันการจองตรงตามจุดต่ำสุดของเกณฑ์การว่าง
    slot = make_slot(start="09:00", remaining=1)

    # When: ผู้ใช้ยืนยันการจองช่วง 09.00 น.
    res = client.post("/bookings", json={"slot_id": slot.id}, headers=AUTH)

    # Then: บันทึกการจองสำเร็จ, แสดงหมายเลขคิว, และที่นั่งว่างของช่วงนั้นลดจาก 1 เป็น 0
    assert res.status_code == 201
    body = res.json()
    assert body["queue_no"]

    slot_after = db.get(Slot, slot.id)
    assert slot_after.remaining == 0


def test_TC_BKG_01_3_booking_requires_verified_identity(client, make_slot):
    """TC-BKG-01-3: ต้องยืนยันตัวตนก่อนจอง"""
    # Given: ผู้รับบริการยังไม่ได้ผ่านการยืนยันตัวตนตาม IF-IDP-01
    slot = make_slot(start="09:00", remaining=1)

    # When: ผู้ใช้พยายามยืนยันการจองช่วง 09.00 น. โดยไม่มี Authorization header
    res = client.post("/bookings", json={"slot_id": slot.id})

    # Then: ระบบต้องปฏิเสธการสร้างบันทึกการจองก่อนจอง; ไม่มีหมายเลขคิวถูกออกสำหรับรายการนี้
    assert res.status_code == 401
    assert res.json()["detail"] == "ยังไม่ได้ยืนยันตัวตน"
