import pytest

# Design a function that pluralizes a given word by adding "s"

# String -> String
# Append "s" to given string
def pluralize(s:str) -> str:
    if type(s) != str:
        raise Exception("Input must be of type str!")
    return s + "s"

def test_pluralize():
    assert pluralize("cat") == "cats"


class TestClass:
    def test_one(self):
        assert pluralize("cat") == "cats"

    def test_two(self):
        assert pluralize("qwerty") == "qwertys"

    def test_three(self):
        assert pluralize("cats") == "catss"

    def test_four(self):
        with pytest.raises(Exception) as error_info:
            assert pluralize(1)

    def test_five(self):
        assert pluralize("dog") != "dog"

    def test_six(self):
        assert pluralize("") == "s"
