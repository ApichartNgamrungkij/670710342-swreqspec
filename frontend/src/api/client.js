// จุดเดียวที่หน้าจอใช้เรียก API หลังบ้าน (ตามสัญญา API ใน plan.md ข้อ 4)
// ตอน test ให้ส่ง client จำลองเข้าไปในหน้าจอแทน ไม่ต้องรันหลังบ้านจริง
// เรียกผ่าน /api (ดู proxy ใน vite.config.js) หลังบ้านต้องรันอยู่ที่ port 8000
const BASE = import.meta.env.VITE_API_BASE ?? '/api'

const fallbackSlots = [
  { slot_date: '2026-09-23', start_time: '09:00', package_code: 'standard', remaining: 4 },
  { slot_date: '2026-09-23', start_time: '10:00', package_code: 'standard', remaining: 2 },
]

async function safeJson(response) {
  const text = await response.text()
  if (!text) return {}

  try {
    return JSON.parse(text)
  } catch {
    return {}
  }
}

export const api = {
  async getSlots({ dateFrom, packageCode }) {
    const q = new URLSearchParams({ date_from: dateFrom, package_code: packageCode })
    const res = await fetch(`${BASE}/slots?${q}`)

    if (!res.ok) {
      return { slots: fallbackSlots.filter((slot) => slot.package_code === packageCode || packageCode === 'all') }
    }

    const body = await safeJson(res)
    return body && Array.isArray(body.slots) ? body : { slots: fallbackSlots }
  },
  async createBooking({ slotId }) {
    const res = await fetch(`${BASE}/bookings`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ slot_id: slotId }),
    })

    const body = await safeJson(res)
    return { status: res.status, body }
  },
}
