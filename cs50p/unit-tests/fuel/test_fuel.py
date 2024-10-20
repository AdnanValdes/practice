import pytest
from fuel import gauge, convert


def test_convert_big_x():
    with pytest.raises(ValueError):
        convert("4/2")
        convert("1/-1")


def test_convert_zero_y():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
        convert("0/0")
        convert("-1/0")


def test_convert_ints():
    with pytest.raises(ValueError):
        convert("1.0/2.0")
        convert("cat/dog")


def test_gauge():
    assert gauge(1) == "E"
    assert gauge(100) == "F"
    assert gauge(50) == "50%"
