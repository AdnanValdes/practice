import pytest
from jar import Jar

def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert Jar(20).capacity == 20
    assert Jar(0).capacity == 0
    with pytest.raises(ValueError):
        Jar(-2)

def test_deposit():
    j1 = Jar()
    assert j1.size == 0
    j1.deposit(1)
    assert j1.size == 1
    j1.deposit(11)
    assert j1.size == 12
    with pytest.raises(ValueError):
        j1.deposit(1)

def test_withdraw():
    j1 = Jar()
    j1.deposit(12)
    j1.withdraw(1)
    assert j1.size == 11
    with pytest.raises(ValueError):
        j1.withdraw(20)

    j2 = Jar()
    j2.deposit(1)
    j2.withdraw(1)
    assert j2.size == 0

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"
