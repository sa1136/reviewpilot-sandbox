from datetime import datetime

from scheduling import duration_minutes, hash_booking_pin, overlaps, slots_for_day


def test_first_slot_is_opening_time():
    assert slots_for_day(datetime(2026, 3, 2))[0].hour == 9


def test_overlaps():
    a = datetime(2026, 3, 2, 9)
    b = datetime(2026, 3, 2, 10)
    c = datetime(2026, 3, 2, 11)
    assert overlaps(a, c, b, c)
    assert not overlaps(a, b, b, c)


def test_duration_one_hour():
    assert duration_minutes(datetime(2026, 3, 2, 9), datetime(2026, 3, 2, 10)) == 60


def test_hash_is_stable():
    assert hash_booking_pin("1234") == hash_booking_pin("1234")
