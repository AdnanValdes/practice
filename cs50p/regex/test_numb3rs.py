import pytest
from numb3rs import validate

# PROGRAM EXPECTS FOUR OCTET IPv4 ADDRESSES

def test_correct_validate():
    assert validate("1.1.1.1") == True
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True
    assert validate("249.249.249.249") == True
    assert validate("192.168.0.42") == True
    assert validate("64.78.200.1") == True
    assert validate("0.0.0.0") == True


def test_wrong_validate():
    assert validate("256.0.0.0") == False
    assert validate("1111.1.1.1") == False
    assert validate("300.1.1.1") == False
    assert validate("cat") == False
    assert validate("123.125.123.643") == False
    assert validate("1.1") == False
