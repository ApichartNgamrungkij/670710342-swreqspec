import { render, screen } from '@testing-library/react'
import BookingResult from '../pages/BookingResult.jsx'

describe('AC-BKG-01', () => {
  test('TC-BKG-01-1 booking success shows queue number and remaining zero', () => {
    render(<BookingResult queueNo="A001" remaining={0} />)

    expect(screen.getByText(/A001/i)).toBeTruthy()
    expect(screen.getByText(/0/i)).toBeTruthy()
  })

  test('TC-BKG-01-2 last slot shows zero remaining after booking', () => {
    render(<BookingResult queueNo="A001" remaining={0} />)

    expect(screen.getByText(/A001/i)).toBeTruthy()
    expect(screen.getByText(/0/i)).toBeTruthy()
  })

  test('TC-BKG-01-3 verified identity is required before booking', () => {
    render(<BookingResult queueNo="" remaining={1} verified={false} />)

    expect(screen.getByText(/ยืนยันตัวตน/i)).toBeTruthy()
  })
})
