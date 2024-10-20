def main():
    """
    program that prompts the user for a fraction, formatted as X/Y,
    wherein each of X and Y is an integer, and then outputs, as a percentage
    rounded to the nearest integer, how much fuel is in the tank.
    If, though, 1% or less remains, output E instead to indicate
    that the tank is essentially empty.
    And if 99% or more remains, output F instead to indicate
    that the tank is essentially full.
    """
    totalizer = check_fuel()
    if totalizer <= 1:
        print("E")
    elif totalizer >= 99:
        print("F")
    else:
        print(str(totalizer) + "%")


def check_fuel():
    fuel = input("Fraction: ")

    try:
        x, y = map(int, fuel.split("/"))
        if x <= y and y != 0:
            return round(x / y * 100)
        else:
            return check_fuel()
    except (ValueError, ZeroDivisionError):
        return check_fuel()


if __name__ == "__main__":
    main()
