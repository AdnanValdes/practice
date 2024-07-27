import pytest
from lines import count_line, is_valid_file, parse_file


def test_count_line():
    """
    Test function that checks for
    empty strings and comments
    """
    assert count_line(" # alsdjfas") == True
    assert count_line("  ") == True
    assert count_line("def test") == False

# Testing for existence of filename extension
def test_is_valid_file():
    assert is_valid_file("foo.py") == True
    assert is_valid_file("foo.txt") == True
    assert is_valid_file("foo.json") == True
    for file in ["foo", "foo.bar", "foo,py"]:
        with pytest.raises(SystemExit) as err:
            is_valid_file(file)
        assert err.type == SystemExit
        assert err.value.code == "Not a Python file"
