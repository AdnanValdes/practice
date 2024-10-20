import pytest
from working import convert


test_values = {
    "9 AM to 5 PM": "09:00 to 17:00",
    "9:00 AM to 5:00 PM": "09:00 to 17:00",
    "10 AM to 8:50 PM": "10:00 to 20:50",
    "10:30 PM to 8 AM": "22:30 to 08:00",
}


def test_convert_time():
    for time in test_values:
        assert convert(time) == test_values[time]


def test_convert_errors():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")
        convert("9 AM - 5 PM")
        convert("09:00 AM - 17:00 PM")
