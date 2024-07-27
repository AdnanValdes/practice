import pytest
from twittr import is_vowel, shorten


def test_is_vowel():
    assert is_vowel("a") == True
    assert is_vowel("A") == True
    assert is_vowel("n") == False


def test_shorten_vowels():
    assert shorten("Hello") == "Hll"
    assert shorten("AEIOU") == ""


def test_shorten_cases():
    assert shorten("adnan") == "dnn"
    assert shorten("ADNAN") == "DNN"


def test_shorten_consonants():
    assert shorten("smrt") == "smrt"


def test_shorten_numbers():
    assert shorten("12345") == "12345"
