import pytest
from twttr import is_vowel, shorten



def test_upper_consonant():
    assert shorten("B") == "B"

def test_punctuation():
    assert shorten(".") == "."


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
