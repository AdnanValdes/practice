import pytest
from um import count

def test_um():
    assert count("um") == 1
    assert count("um?") == 1
    assert count("um um um") == 3
    assert count("um? um! um.") == 3
    assert count("UM!") == 1

def test_um_sentence():
    assert count("Um, thanks for the album.") == 1
    assert count("Um, thanks, um...") == 2

def test_no_um():
    assert count("yummy") == 0
    assert count("This is so yummy!") == 0
