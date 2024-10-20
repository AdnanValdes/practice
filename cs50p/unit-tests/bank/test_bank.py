import pytest
from bank import value


def test_value_hello():
    assert value("hello") == 0


def test_value_h():
    assert value("h") == 20
    assert value("hi") == 20
    assert value("h231asdf") == 20


def test_value_other():
    assert value("ah") == 100
    assert value("1h") == 100
