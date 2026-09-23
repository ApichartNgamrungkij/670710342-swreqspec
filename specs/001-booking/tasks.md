# Feature: จองคิวตรวจสุขภาพ (Booking)
Spec ID: SPEC-BKG-001
อ้างอิง plan.md: specs/001-booking/plan.md
วันที่: 2569-09-23

สรุป:
- งานนี้มี 11 task ทั้งหมด และมี 2 task ที่ต้องรอ Open Questions
- Open Question ที่ยังค้างอยู่คือ Q-02 ว่าหมายเลขคิวจะรีเซ็ตวันละเท่าไหร่และมีรูปแบบอย่างไร เพื่อให้การออกหมายเลขคิวสามารถตรึงกติกาได้ก่อนยืนยัน

### T-01 สร้างโครงฐานข้อมูลและ migration อย่างครบถ้วน
- รองรับ: CON-TECH-01, DOM-PDPA-01, IF-HIS-01
- ตรวจด้วย: ไม่มี AC ตรง ๆ เป็นงานพื้นฐานของ T-01
- ไฟล์ที่แตะ: backend/app/db/models.py, backend/app/db/session.py, backend/app/db/migrations/001_init.py, backend/app/config.py
- ต้องทำหลัง: ไม่มี
- เสร็จเมื่อ: migration สร้างตาราง slots, bookings, audit_logs และคอนฟิกฐานข้อมูล PostgreSQL ใช้ได้ใน test SQLite ในหน่วยความจำ
- สถานะ: เสร็จ รอทีมตรวจ

### T-02 สร้าง API ค้นช่วงเวลาว่างและคำนวณช่วงใกล้เคียงตามแพ็กเกจ
- รองรับ: FR-BKG-01, FR-BKG-06, NFR-PERF-01
- ตรวจด้วย: AC-BKG-05
- ไฟล์ที่แตะ: backend/app/slots/router.py, backend/app/slots/service.py, backend/tests/test_AC_BKG_05.py
- ต้องทำหลัง: T-01
- เสร็จเมื่อ: GET /slots คืนรายการช่วงเวลาและจำนวนที่นั่งคงเหลือแบบ p95 ภายใต้เงื่อนไข 200 คนพร้อมกัน และคำนวณช่วงเวลาที่สอดคล้องกับแพ็กเกจที่เลือกได้
- สถานะ: พร้อมทำ

### T-03 สร้างหน้าเลือกแพ็กเกจและช่วงเวลาแบบใช้ API จำลอง
- รองรับ: FR-BKG-01, FR-BKG-06
- ตรวจด้วย: ไม่มี AC ตรง ๆ เป็นงานพื้นฐานของ T-03
- ไฟล์ที่แตะ: frontend/src/pages/SlotPicker.jsx, frontend/src/api/client.js, frontend/src/__tests__/SlotPicker.test.jsx
- ต้องทำหลัง: ไม่มี
- เสร็จเมื่อ: หน้าจอแสดงวันและช่วงเวลาที่ว่าง พร้อมตัวเลือกแพ็กเกจ และแสดงผลที่นั่งคงเหลือตาม API จำลองที่กำหนดไว้
- สถานะ: เสร็จ 

### T-04 สร้าง API จองคิวพื้นฐานและบันทึก booking พร้อมคอลัมน์ queue_no placeholder
- รองรับ: FR-BKG-04, IF-HIS-01, IF-NOT-01
- ตรวจด้วย: AC-BKG-01
- ไฟล์ที่แตะ: backend/app/booking/router.py, backend/app/booking/service.py, backend/tests/test_AC_BKG_01.py
- ต้องทำหลัง: T-01, T-02
- เสร็จเมื่อ: POST /bookings บันทึกการจอง ตัดจำนวนที่นั่ง และคืนค่า booking id พร้อม queue_no placeholder ที่ยังไม่ตัดสินกติกา Q-02
- สถานะ: รอ Q-02

### T-05 สร้างกฎป้องกันจองซ้ำในวันเดียวกันและคืนหมายเลขคิวเดิม
- รองรับ: FR-BKG-02
- ตรวจด้วย: AC-BKG-02
- ไฟล์ที่แตะ: backend/app/booking/service.py, backend/tests/test_AC_BKG_02.py
- ต้องทำหลัง: T-04
- เสร็จเมื่อ: เมื่อผู้รับบริการมีคิวที่ยังไม่ได้ใช้ในวันเดียวกัน ระบบปฏิเสธการจองใหม่และส่งกลับหมายเลขคิวเดิมตามข้อมูล booking ที่มีอยู่
- สถานะ: พร้อมทำ

### T-06 สร้างกฎเสนอช่วงใกล้เคียง 3 ตัวเลือกเมื่อช่วงเวลาที่เลือกเต็ม
- รองรับ: FR-BKG-03
- ตรวจด้วย: AC-BKG-03
- ไฟล์ที่แตะ: backend/app/slots/service.py, backend/app/booking/service.py, backend/tests/test_AC_BKG_03.py
- ต้องทำหลัง: T-02, T-04
- เสร็จเมื่อ: เมื่อตรงช่วงที่เลือกเต็มและมีช่วงย้ายของวันเดียวกัน/วันถัดไปอย่างน้อย 3 ตัว ระบบส่ง 409 พร้อม 3 ตัวเลือกที่ใกล้ที่สุด และไม่สร้างรายการจองซ้อน
- สถานะ: พร้อมทำ

### T-07 สร้างหน้าจอยืนยันและแสดงข้อความ “ช่วงเวลาเต็ม” พร้อม 3 ตัวเลือก
- รองรับ: FR-BKG-03, FR-BKG-04
- ตรวจด้วย: AC-BKG-03
- ไฟล์ที่แตะ: frontend/src/pages/ConfirmBooking.jsx, frontend/src/__tests__/AC-BKG-03.test.jsx
- ต้องทำหลัง: T-03, T-06
- เสร็จเมื่อ: หน้ายืนยันแสดงข้อความ “ช่วงเวลาเต็ม” พร้อม 3 ตัวเลือกให้ผู้ใช้เลือกใหม่ และไม่สร้าง booking ซ้อนขณะยืนยัน
- สถานะ: พร้อมทำ

### T-08 สร้างคิวส่งข้อความยืนยันและส่งซ้ำภายใน 5 นาทีเมื่อส่งไม่สำเร็จ
- รองรับ: FR-BKG-05, IF-NOT-01, NFR-REL-02
- ตรวจด้วย: AC-BKG-04
- ไฟล์ที่แตะ: backend/app/notify/queue.py, backend/app/booking/service.py, backend/tests/test_AC_BKG_04.py
- ต้องทำหลัง: T-04
- เสร็จเมื่อ: การยืนยันการจองยังบันทึกได้แม้ส่งข้อความไม่สำเร็จ และมีรายการงานส่งซ้ำที่กำหนดภายใน 5 นาที
- สถานะ: พร้อมทำ

### T-09 สร้าง audit log สำหรับเข้าถึงข้อมูลการจองและการอ่านรายละเอียดการจอง
- รองรับ: DOM-PDPA-01, FR-BKG-05
- ตรวจด้วย: AC-BKG-06
- ไฟล์ที่แตะ: backend/app/audit/middleware.py, backend/app/booking/router.py, backend/tests/test_AC_BKG_06.py
- ต้องทำหลัง: T-01, T-04
- เสร็จเมื่อ: ทุกการเข้าถึงข้อมูลการจองถูกบันทึก audit log ที่มี actor_id, accessed_at, hn และสามารถดูรายละเอียดการจองได้ผ่าน GET /bookings/{id}
- สถานะ: พร้อมทำ

### T-10 นำระบบยืนยันตัวตนและข้อมูลผู้รับบริการจาก HIS มาใช้ใน flow จองคิว
- รองรับ: IF-IDP-01, IF-HIS-01
- ตรวจด้วย: ไม่มี AC ตรง ๆ เป็นงานพื้นฐานของ T-10
- ไฟล์ที่แตะ: backend/app/auth/idp.py, backend/app/his/client.py, backend/app/booking/router.py
- ต้องทำหลัง: T-01
- เสร็จเมื่อ: ทุก endpoint ที่เกี่ยวกับข้อมูลผู้รับบริการตรวจสอบผลยืนยันตัวตนก่อน และการค้นหา HN จาก HIS ทำได้โดยไม่เก็บเลขบัตรประชาชนในตารางการจอง
- สถานะ: พร้อมทำ

### T-11 ต่อหน้าจอกับ API จริงหลังจาก backend และ flow เต็มครบแล้ว
- รองรับ: FR-BKG-01, FR-BKG-03, FR-BKG-04
- ตรวจด้วย: ไม่มี AC ตรง ๆ เป็นงานพื้นฐานของ T-11
- ไฟล์ที่แตะ: frontend/src/App.jsx, frontend/src/pages/SlotPicker.jsx, frontend/src/pages/ConfirmBooking.jsx, frontend/src/pages/BookingResult.jsx, frontend/src/api/client.js
- ต้องทำหลัง: T-02, T-06, T-07
- เสร็จเมื่อ: หน้าจอใช้ API จริงในการโหลดช่วงเวลาและยืนยันการจอง พร้อมแสดงหมายเลขคิวจาก response ที่ได้รับจริง
- สถานะ: รอ Q-02

### ตารางตรวจความครบ AC
| AC ID | task ที่ตรวจ AC นี้ |
|---|---|
| AC-BKG-01 | T-04 |
| AC-BKG-02 | T-05 |
| AC-BKG-03 | T-06, T-07 |
| AC-BKG-04 | T-08 |
| AC-BKG-05 | T-02 |
| AC-BKG-06 | T-09 |

### ตารางตรวจความครบ Constraint
| Constraint ID | task ที่ทำให้เป็นจริง |
|---|---|
| CON-TECH-01 | T-01 |
| DOM-PDPA-01 | T-09 |
| IF-IDP-01 | T-10 |
| IF-HIS-01 | T-01, T-10 |
| IF-NOT-01 | T-04, T-08 |

### สิ่งที่ยังไม่ทำ
- Q-02 หมายเลขคิวรีเซ็ตรายวัน หรือนับต่อเนื่อง และมีรูปแบบอย่างไร (เช่น A001)? -> ถามเจ้าหน้าที่เวชระเบียน (ยังไม่ได้คำตอบ)
  - รออยู่ที่: T-04, T-11
