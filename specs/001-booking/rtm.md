# RTM: จองคิวตรวจสุขภาพ (Booking)
อ้างอิง: spec.md SPEC-BKG-001 Draft v2 | tasks.md | test-cases.md
สร้างด้วย /verify เมื่อ 2569-10-07 08:30 | test: 6 ผ่าน 1 ไม่ผ่าน

## 1. ตามรอยไปข้างหน้า (requirement ไป โค้ด ไป test)
| ID | AC | task | โค้ด (ไฟล์: ฟังก์ชัน) | test (ผล) | สถานะ |
|---|---|---|---|---|---|
| FR-BKG-01 | AC-BKG-05 | T-02 | backend/app/slots/router.py:get_slots; backend/app/slots/service.py:list_available_slots | backend/tests/test_AC_BKG_05.py: passed | ครบ |
| FR-BKG-02 | AC-BKG-02 | T-04 | backend/app/booking/service.py:create_booking (ไม่มีการตรวจ booking ในวันเดียวกัน) | ไม่มี test | ยังไม่ถึง |
| FR-BKG-03 | AC-BKG-03 | T-05, T-11, T-12 | ไม่มีการคำนวณช่วงแทนที่/คำเตือนเต็มในโค้ด | ไม่มี test | ยังไม่ถึง |
| FR-BKG-04 | AC-BKG-01 | T-03, T-06 | backend/app/booking/service.py:create_booking; backend/app/booking/router.py:create_booking | backend/tests/test_AC_BKG_01.py: 3 passed | ครบ |
| FR-BKG-05 | AC-BKG-04 | T-07 | ไม่มีคิวส่งข้อความและไม่มี retry logic | ไม่มี test | ยังไม่ถึง |
| FR-BKG-06 | ไม่มี AC | T-02 | backend/app/slots/router.py:get_slots; backend/app/slots/service.py:list_available_slots | backend/tests/test_AC_BKG_05.py: passed | ครบ |
| NFR-PERF-01 | AC-BKG-05 | T-02 | backend/app/slots/service.py:list_available_slots | backend/tests/test_AC_BKG_05.py: passed | ครบ |
| NFR-SEC-01 | ไม่มี AC | ไม่มี task | ไม่มี TLS / HTTPS / secure transport setup ใน codebase | ไม่มี test | ยังไม่ถึง |
| NFR-REL-02 | AC-BKG-04 | T-07 | ไม่มี retry queue สำหรับข้อความ | ไม่มี test | ยังไม่ถึง |
| NFR-USE-01 | ไม่มี AC | ไม่มี task | ไม่มี UX/flow validation ใน UI | ไม่มี test | ยังไม่ถึง |
| CON-TECH-01 | ไม่มี AC | T-01 | backend/app/config.py:DATABASE_URL; backend/app/db/session.py:engine | ไม่มี test ที่ตรวจ PostgreSQL | ช่องโหว่ |
| DOM-PDPA-01 | AC-BKG-06 | T-08 | ไม่มี audit middleware หรือบันทึก log ในbackend/app/ | ไม่มี test | ยังไม่ถึง |
| IF-IDP-01 | ไม่มี AC | T-03 | backend/app/auth/idp.py:get_verified_hn | backend/tests/test_AC_BKG_01.py: 1 passed (authenticated case) | ครบ |
| IF-HIS-01 | ไม่มี AC | T-09 | backend/app/booking/router.py:BookingRequest.national_id (field only); ไม่มี HIS client | ไม่มี test | ยังไม่ถึง |
| IF-NOT-01 | AC-BKG-04 | T-07 | ไม่มี async queue / retry sender | ไม่มี test | ยังไม่ถึง |
| AC-BKG-01 | AC-BKG-01 | T-03, T-06 | backend/app/booking/router.py:create_booking; backend/app/booking/service.py:create_booking | backend/tests/test_AC_BKG_01.py: 3 passed | ครบ (หลังบ้าน) |
| AC-BKG-02 | AC-BKG-02 | T-04 | backend/app/booking/service.py:create_booking (เงื่อนไขซ้ำไม่ตรวจ) | ไม่มี test | ยังไม่ถึง |
| AC-BKG-03 | AC-BKG-03 | T-05, T-11, T-12 | ไม่มี flow ช่วงเวลาเต็ม/3 ตัวเลือก | ไม่มี test | ยังไม่ถึง |
| AC-BKG-04 | AC-BKG-04 | T-07 | ไม่มีคิวข้อความและ retry | ไม่มี test | ยังไม่ถึง |
| AC-BKG-05 | AC-BKG-05 | T-02 | backend/app/slots/router.py:get_slots; backend/app/slots/service.py:list_available_slots | backend/tests/test_AC_BKG_05.py: passed | ครบ |
| AC-BKG-06 | AC-BKG-06 | T-08 | absence of audit logging middleware | ไม่มี test | ยังไม่ถึง |

## 2. ตามรอยย้อนกลับ (โค้ด ไป requirement)
| โค้ด (ไฟล์: ฟังก์ชัน หรือ endpoint) | อ้าง ID | ตรงกับข้อความใน spec ไหม | หมายเหตุ |
|---|---|---|---|
| backend/app/booking/service.py:create_booking | FR-BKG-04, FR-BKG-02 | ไม่ครบ | มีการตัดที่นั่งและสร้าง booking แต่ไม่มีการตรวจว่ามีคิวในวันเดียวกัน ดังนั้น FR-BKG-02 ยังไม่ได้ทำ |
| backend/app/slots/service.py:list_available_slots | FR-BKG-01, FR-BKG-06 | ครบบางส่วน | คืน slots ที่ยังมีที่นั่งและกรอง package_code แต่วันกำหนด 14 วันเท่านั้น ไม่ใช่ 30 วันตาม spec |
| backend/app/auth/idp.py:get_verified_hn | IF-IDP-01 | ใช่ | ตรวจ Authorization header และตอบ 401 หากยังไม่ได้ยืนยันตัวตน |
| backend/app/config.py:DATABASE_URL | CON-TECH-01 | ไม่ครบ | ค่าเริ่มต้นเป็น sqlite:///./dev.db หากไม่มี DATABASE_URL จะไม่ใช้ PostgreSQL ตามข้อกำหนด |
| backend/app/booking/router.py:BookingRequest | IF-HIS-01 | ไม่ครบ | มี field national_id แต่ไม่มีการค้น HIS หรือแปลงเป็น HN; ระวังการคงข้อมูลที่ห้ามเก็บ |
| backend/app/main.py:app | DOM-PDPA-01 | ไม่ครบ | ไม่มี middleware สำหรับ audit log แต่มีตาราง audit_logs ใน schema |
| frontend/src/__tests__/AC-BKG-01.test.jsx | AC-BKG-01 | ไม่ครบ | import ไปยัง frontend/src/pages/BookingResult.jsx แต่ไฟล์ไม่มีอยู่จริง จึงเป็น UI ที่ยังไม่ได้สร้าง |

## 3. ข้อค้นพบ
ชนิด: AC ไม่มี test / test อ่อน / โค้ดไม่มี FR / FR ไม่มี AC / เดา Q-xx / ละเมิด Constraint / ตัวเลขไม่ตรง spec / อ้าง ID ผิดเรื่อง
ทีมตัดสิน: แก้โค้ด / แก้ spec / เพิ่ม Q-xx / ไม่ใช่ปัญหา (พร้อมเหตุผล 1 บรรทัด)

| F-ID | ชนิด | อยู่ที่ | ขัดกับ | รายละเอียด | ทีมตัดสิน |
|---|---|---|---|---|---|
| F-001 | AC ไม่มี test / test อ่อน | frontend/src/__tests__/AC-BKG-01.test.jsx; frontend/src/pages | AC-BKG-01, FR-BKG-04 | ไฟล์หน้าแสดงหมายเลขคิวที่ test import ไปยัง frontend/src/pages/BookingResult.jsx ไม่มีอยู่จริง และ test ทั้ง 3 ตัวใน frontend ล้มเพราะ UI ยังไม่สร้าง | แก้โค้ด |
| F-002 | ละเมิด Constraint | backend/app/config.py:DATABASE_URL | CON-TECH-01 | ค่าเริ่มต้นเป็น SQLite ซึ่งตรงข้ามกับข้อกำหนดว่าใช้ PostgreSQL ตามมาตรฐานฝ่าย IT ของโรงพยาบาล | แก้โค้ด |
| F-003 | ตัวเลขไม่ตรง spec | backend/app/slots/service.py:DAYS_AHEAD | FR-BKG-01 | spec กำหนดแสดง 30 วันข้างหน้า แต่โค้ดใช้ 14 วัน และ task ท้ายไฟล์ระบุแค่ช่วงย่อส่วน 14 วัน จึงไม่ตรงข้อกำหนดที่ระบุว่า 30 วัน | แก้ spec / แก้โค้ด |

## 4. แก้แล้ว
| F-ID | แก้อย่างไร | รู้ได้อย่างไร |
|---|---|---|
| - | ไม่มีข้อค้นพบเดิมใน rtm.md | ไม่มี rtm.md เดิม |
