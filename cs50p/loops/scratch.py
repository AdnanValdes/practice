def valid_zeros(s):
    """
    The first number used cannot be a 0.
    """

    # Check if any zeroes in string
    if "0" not in s:
        return True

    # Find first number
    first_num = None
    for i in s:
        if i.isdigit():
            if first_num == "0":
                return True

    return False


print(valid_zeros("AA2222"))
