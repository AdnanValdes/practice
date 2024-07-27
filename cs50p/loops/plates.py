import string


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    return all(
        [character_limits(s), are_numbers_at_end(s), valid_zeroes(s), no_punctuation(s)]
    )


def character_limits(s):
    """
    Checks if input lenght is between 2 and 6 chars inclusive.
    If so, returns True iff the first two characters are letters.
    """
    l = len(s)
    if l > 1 and l < 7:
        # Slice list for first two chars
        return s[:2].isalpha()
    return False


def are_numbers_at_end(s):
    """
    Numbers cannot be used in the middle of a plate; they must come at the end.
    For example, AAA222 would be an acceptable vanity plate;
    AAA22A would not be acceptable.
    """
    # Check if there are numbers in string
    for i in range(len(s)):
        if s[i].isdigit():
            # Check that the numbers are at the end
            return s[i:].isdigit()
    return True


def valid_zeroes(s):
    """
    The first number used cannot be a 0.
    """

    # Check if any zeroes in string
    if "0" not in s:
        return True

    for i in range(len(s)):
        if s[i].isdigit():
            return not (s[i] == "0" and s[i:].isdigit())


def no_punctuation(s):
    return not any(punct in string.punctuation for punct in s)


main()
