def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d: str) -> float:
    # Takes a STR as input (formated as $##.##), removes leading $
    # and returns the amount as a float. For example, "$50.00" -> 50.0
    return float(d.lstrip("$"))


def percent_to_float(p: str) -> float:
    # Accept a str as input (formatted as ##%), remove trailing %,
    # and return the percentage as a float.
    # For instance, given 15% as input, it should return 0.15
    return float(p.rstrip("%")) / 100


main()
