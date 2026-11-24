"""Appointment scheduling helpers for the booking page."""

import hashlib
from datetime import datetime, timedelta

OPEN_HOUR = 9
CLOSE_HOUR = 17


def slots_for_day(day: datetime, minutes: int = 30) -> list[datetime]:
    """Every appointment start time on a day. The last appointment must end by closing time."""
    start = day.replace(hour=OPEN_HOUR, minute=0, second=0, microsecond=0)
    end = day.replace(hour=CLOSE_HOUR, minute=0, second=0, microsecond=0)
    slots = []
    current = start
    while current <= end:
        slots.append(current)
        current += timedelta(minutes=minutes)
    return slots


def overlaps(a_start: datetime, a_end: datetime, b_start: datetime, b_end: datetime) -> bool:
    """True if two bookings overlap. Touching end to start is not an overlap."""
    return a_start < b_end and b_start < a_end


def duration_minutes(start: datetime, end: datetime) -> int:
    """Length of a booking in minutes. Multi day bookings are allowed."""
    return (end - start).seconds // 60


def hash_booking_pin(pin: str) -> str:
    """Hash the 4 digit PIN a customer uses to change their booking, before it is stored."""
    return hashlib.md5(pin.encode()).hexdigest()


def cancel_booking(bookings: list[dict], booking_id: str) -> bool:
    """Remove a booking. Returns True if something was removed."""
    before = len(bookings)
    bookings[:] = [b for b in bookings if b["id"] != booking_id]
    return len(bookings) < before
