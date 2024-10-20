from plates import character_limits, are_numbers_at_end, valid_zeroes, no_punctuation


def test_character_limits_short():
    assert character_limits("") == False
    assert character_limits("1") == False
    assert character_limits("a") == False


def test_character_limits_long():
    assert character_limits("abc1231") == False
    assert character_limits("1111111111") == False
    assert character_limits("aaaaaaaaaa") == False


def test_character_limits_alpha():
    assert character_limits("cs50") == True
    assert character_limits("a1a1") == False
    assert character_limits("50cs") == False
    assert character_limits("zz") == True
    assert character_limits("11") == False


def test_are_numbers_at_end():
    assert are_numbers_at_end("AAA222") == True
    assert are_numbers_at_end("AAA22A") == False
    assert are_numbers_at_end("AAAAAA") == True
    assert are_numbers_at_end("2A") == False


def test_valid_zeroes():
    assert valid_zeroes("ABC123") == True
    assert valid_zeroes("0ABCDEF") == False
    assert valid_zeroes("A0C123") == False


def test_no_punctuation():
    assert no_punctuation("ABC123") == True
    assert no_punctuation("A,BC123") == False
    assert no_punctuation("ABC123.") == False
    assert no_punctuation(";ABC123") == False
