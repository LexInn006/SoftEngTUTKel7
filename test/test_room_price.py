import pytest
from src.rules import compute_room_price


def test_guest_adult():
    assert compute_room_price(
        guest_age=34,
        room_type="standard",
        booking_day="weekday",
        stay_duration=3
    ) == 2700000



def test_invalid_age():
    with pytest.raises(ValueError):
        compute_room_price(
        guest_age=-10,
        room_type="standard",
        booking_day="weekday",
        stay_duration=3
        )