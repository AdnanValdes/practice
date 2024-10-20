def main():
    """
    a program that prompts the user for an arithmetic expression and then
    calculates and outputs the result as a floating-point value formatted
    to one decimal place. Assume that the user’s input will be formatted as
    x y z, with one space between x and y and one space between y and z,
    wherein:

        x is an integer
        y is +, -, *, or /
        z is an integer
    """

    # Accept user math expression
    exp = input("Expression: ")

    # Sanitize and split expression
    x, y, z = sanitizeExp(exp)

    # Convert x and z to floats
    x, z = toFloat(x, z)

    # Check for division by zero
    if isZero(y, z):
        print("Can't divide by zero!")
        quit()

    print(calculate(x, y, z))


def sanitizeExp(exp: str) -> list:
    return exp.strip().split()


def toFloat(x: str, z: str) -> list:
    return float(x), float(z)


def isZero(y: str, z: str) -> bool:
    return True if z == 0 and y == "/" else False


def calculate(x: float, y: str, z: float) -> float:
    operations = {"+": x + z, "-": x - z, "*": x * z, "/": x / z}
    return operations[y]


main()
