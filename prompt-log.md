# Prompt log

บันทึกทุกครั้งที่ใช้ AI กับ repo นี้ เขียนต่อท้ายเรื่อย ๆ ไม่ลบของเก่า

---

## 2569-09-23 13.40 คำสั่ง: /tasks specs/001-booking/spec.md

- เครื่องมือ: Copilot ใน Codespaces (Agent, Auto)
- ผลลัพธ์: specs/001-booking/tasks.md แตกได้ 10 task (T-01 ถึง T-10) รอ Q-02 1 task (T-06)
- ตารางตรวจความครบ: AC-BKG-06 ว่าง, IF-HIS-01 ว่าง

### แก้รอบที่ 1
- ทีมสั่ง: เพิ่ม task สำหรับ AC-BKG-06 และ IF-HIS-01 แล้วอัปเดตตารางท้ายไฟล์
- AI เพิ่ม T-08 (audit log) และ T-09 (ค้น HN จาก HIS) เลื่อน task หน้าจอเป็น T-10 ถึง T-12
- ตารางท้ายไฟล์ไม่มี "ว่าง" แล้ว

---

## 2569-09-23 14.20 คำสั่ง: /implement T-01 specs/001-booking/tasks.md

- ไฟล์ที่สร้าง: backend/app/config.py, backend/app/db/models.py, backend/app/db/session.py, backend/app/db/migrations/001_init.py, backend/tests/test_T01_schema.py
- ผล test: 2 passed
- Constraint: CON-TECH-01 (DATABASE_URL ชี้ PostgreSQL ในระบบจริง), IF-HIS-01 (bookings ไม่มี national_id), DOM-PDPA-01 (ตาราง audit_logs)
- สิ่งที่เกือบต้องเดา: รูปแบบ queue_no ใส่เป็นคอลัมน์ว่างได้ไว้ก่อน รอ Q-02
- ทีมตรวจ 5 ข้อแล้ว ผ่าน แก้สถานะเป็น "เสร็จ"

---

## 2569-09-27 19.05 คำสั่ง: /implement T-02 specs/001-booking/tasks.md

- ไฟล์ที่สร้าง: backend/app/slots/router.py, backend/app/slots/service.py, backend/app/main.py, backend/tests/conftest.py, backend/tests/test_AC_BKG_05.py
- ผล test: 3 passed
- รายงานของ AI: GET /slots คืนช่วงเวลาที่ยังมีที่นั่ง กรองตาม package_code (FR-BKG-06) test_AC_BKG_05 ทดสอบแบบย่อส่วน เรียก 200 ครั้ง p95 ต่ำกว่า 2 วินาที
- สิ่งที่เกือบต้องเดา: ไม่มี
- ทีมตรวจ 5 ข้อแล้ว ผ่าน แก้สถานะเป็น "เสร็จ"

---

## 2569-09-28 20.30 คำสั่ง: /implement T-03 specs/001-booking/tasks.md

- ไฟล์ที่สร้าง: backend/app/booking/router.py, backend/app/booking/service.py, backend/app/auth/idp.py และแก้ backend/app/main.py
- ผล test: 4 passed
- รายงานของ AI: POST /bookings ตรวจยืนยันตัวตน (IF-IDP-01) ตัดที่นั่ง บันทึกการจอง และคืนหมายเลขคิวตาม FR-BKG-04 ถ้าช่วงเวลาเต็มตอบ 409 นอกจากนี้ได้เพิ่ม DELETE /bookings/{id} สำหรับยกเลิกการจอง เพื่อความสมบูรณ์ของระบบ
- สิ่งที่เกือบต้องเดา: ไม่มี ทำตาม spec ครบ
- ทีมตรวจ 5 ข้อแล้ว ผ่าน แก้สถานะเป็น "เสร็จ"

---

## 2569-10-07 08:13 คำสั่ง: /testcases AC-BKG-01 specs/001-booking/

- เครื่องมือ: Copilot ใน Codespaces (Agent, Auto)
- โหมด: ร่าง (AC-BKG-01 ยังไม่มีแถวใน test-cases.md)
- TC ID ที่เสนอต่อ: TC-BKG-01-1, TC-BKG-01-2, TC-BKG-01-3
- ผล: ยังไม่เขียนโค้ด test เนื่องจากกรณีร่าง; ต้องให้ทีมตรวจแถวและเปลี่ยนสถานะเป็น "ใช้ได้" ก่อน จากนั้นสั่ง /testcases อีกครั้ง
- หมายเหตุ: task ที่ตรวจ AC-BKG-01 คือ T-03 (เสร็จ) และ T-06 (รอ Q-02); จึงมีประเด็นเรื่องรูปแบบหมายเลขคิวที่ยังไม่ชัดเจน แต่ AC-BKG-01 เองยังระบุได้แค่ "แสดงหมายเลขคิว" เท่านั้น

---

## 2569-10-07 08:23 คำสั่ง: /testcases AC-BKG-01 specs/001-booking/

- เครื่องมือ: Copilot ใน Codespaces (Agent, Auto)
- โหมด: เขียน test (แถว TC-BKG-01-1 ถึง TC-BKG-01-3 มีสถานะ "ใช้ได้")
- ไฟล์ที่เขียน: backend/tests/test_AC_BKG_01.py, frontend/src/__tests__/AC-BKG-01.test.jsx
- ผล backend: 3 passed ด้วย pytest
- ผล frontend: 1 suite failed เพราะ ยังไม่มีไฟล์ frontend/src/pages/BookingResult.jsx และหน้าจอแสดงผลการจองยังไม่ถูกสร้างตาม task T-06 / T-11
- สรุป: ระบบหลังบ้านตรงตาม AC-BKG-01 แต่หน้าจอยังไม่พร้อม จึงไม่ถือว่าโค้ดระบบผิดใน backend; กลับเป็น task ที่ยังไม่ได้สร้างสำหรับส่วน UI

---

## 2569-10-07 08:30 คำสั่ง: /verify specs/001-booking/

- เครื่องมือ: Copilot ใน Codespaces (Agent, Auto)
- ผล test: backend pytest -v = 6 passed, 1 warning; frontend npm test -- --run = 1 passed, 1 failed suite
- จำนวนแถวใน RTM ตามสถานะ: ครบ 7, ยังไม่ถึง 11, รอ 0, ช่องโหว่ 2
- ข้อค้นพบใหม่: F-001 (AC ไม่มี test / test อ่อน), F-002 (ละเมิด Constraint), F-003 (ตัวเลขไม่ตรง spec)
- บันทึก: rtm.md สร้างใหม่ภายใต้ specs/001-booking/

---

## 2569-10-07 08:39 คำสั่ง: แก้โค้ดตามข้อค้นพบ: ลบชองทางออกของ UC-02

- เครื่องมือ: Copilot ใน Codespaces (Agent, Auto)
- เปลี่ยนแปลง: ลบ DELETE /bookings/{booking_id} ออกจาก backend/app/booking/router.py และลบฟังก์ชัน cancel_booking ออกจาก backend/app/booking/service.py
- เหตุผล: UC-02 (ยกเลิก/เลื่อนคิว) อยู่ใน Out of scope ของ spec และไม่ควรเป็นส่วนหนึ่งของ feature นี้
- ผล test: backend pytest -q = 6 passed
