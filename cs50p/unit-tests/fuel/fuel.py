def main():

    fuel = convert(input("Fraction: "))
    print(gauge(fuel))


def convert(fraction: str) -> int:
    """
    expects a str in X/Y format as input, wherein each
    of X and Y is an integer, and returns that fraction
    as a percentage rounded to the nearest int between 0
    and 100, inclusive. If X and/or Y is not an integer,
    or if X is greater than Y, then convert should raise
    a ValueError.
    If Y is 0, then convert should raise a ZeroDivisionError.
    """
    x, y = map(int, fraction.split("/"))
    if y == 0:
        raise ZeroDivisionError
    elif x > y:
        raise ValueError
    return round(x / y * 100)


def gauge(percentage: int) -> str:
    """
    gauge expects an int and returns a str that is:
        "E" if that int is less than or equal to 1,
        "F" if that int is greater than or equal to 99,
        and "Z%" otherwise, wherein Z is that same int.
    """
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return str(percentage) + "%"


if __name__ == "__main__":
    main()
