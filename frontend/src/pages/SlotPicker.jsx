import { useEffect, useState } from 'react'
import { api } from '../api/client.js'

// รองรับ FR-BKG-01 และ FR-BKG-06: หน้าเลือกแพ็กเกจและช่วงเวลาแสดงช่วงเวลาว่างและจำนวนที่นั่งคงเหลือ
export default function SlotPicker() {
  const [packageCode, setPackageCode] = useState('standard')
  const [slots, setSlots] = useState([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    let active = true

    async function loadSlots() {
      setLoading(true)

      try {
        const data = await api.getSlots({ dateFrom: '2026-09-23', packageCode })
        if (active) {
          setSlots(data.slots ?? [])
        }
      } catch {
        if (active) {
          setSlots([])
        }
      } finally {
        if (active) {
          setLoading(false)
        }
      }
    }

    loadSlots()
    return () => {
      active = false
    }
  }, [packageCode])

  return (
    <main className="mx-auto max-w-3xl p-6">
      <h1 className="text-2xl font-bold text-teal-800">เลือกแพ็กเกจและช่วงเวลา</h1>

      <div className="mt-4">
        <label className="block text-sm font-medium text-slate-700">แพ็กเกจ</label>
        <select
          value={packageCode}
          onChange={(event) => setPackageCode(event.target.value)}
          className="mt-2 rounded border border-slate-300 px-3 py-2"
        >
          <option value="standard">standard</option>
          <option value="premium">premium</option>
        </select>
      </div>

      <div className="mt-6 space-y-3">
        {loading ? (
          <p className="text-slate-600">กำลังโหลดช่วงเวลา...</p>
        ) : slots.length === 0 ? (
          <p className="text-slate-600">ไม่มีช่วงเวลาว่าง</p>
        ) : (
          slots.map((slot) => (
            <div key={`${slot.slot_date}-${slot.start_time}`} className="rounded border border-slate-200 p-3">
              <div className="flex items-center justify-between">
                <span className="text-lg font-semibold text-slate-800">{slot.start_time}</span>
                <span className="text-sm text-slate-600">{slot.remaining} ที่นั่งคงเหลือ</span>
              </div>
              <div className="mt-1 text-sm text-slate-500">{slot.slot_date}</div>
            </div>
          ))
        )}
      </div>
    </main>
  )
}
