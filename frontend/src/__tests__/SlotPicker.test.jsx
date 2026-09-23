import { render, screen, waitFor } from '@testing-library/react'
import SlotPicker from '../pages/SlotPicker.jsx'
import { api } from '../api/client.js'

vi.mock('../api/client.js', () => ({
  api: {
    getSlots: vi.fn(),
  },
}))

test('SlotPicker แสดงช่วงเวลาและจำนวนที่นั่งที่ได้รับจาก API จำลอง', async () => {
  api.getSlots.mockResolvedValue({
    slots: [
      { slot_date: '2026-09-23', start_time: '09:00', package_code: 'standard', remaining: 4 },
      { slot_date: '2026-09-23', start_time: '10:00', package_code: 'standard', remaining: 2 },
    ],
  })

  render(<SlotPicker />)

  expect(screen.getByText('เลือกแพ็กเกจและช่วงเวลา')).toBeTruthy()
  await waitFor(() => {
    expect(screen.getByText('09:00')).toBeTruthy()
  })
  expect(screen.getByText('4 ที่นั่งคงเหลือ')).toBeTruthy()
})

test('SlotPicker ไม่ crash เมื่อ API ส่ง 500 หรือ response ว่าง', async () => {
  api.getSlots.mockResolvedValue({ slots: [] })

  render(<SlotPicker />)

  await waitFor(() => {
    expect(screen.getByText('เลือกแพ็กเกจและช่วงเวลา')).toBeTruthy()
  })
  expect(screen.queryByText('กำลังโหลดช่วงเวลา...')).toBeNull()
})
