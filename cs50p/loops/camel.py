def main():
    """
    program that prompts the user for the name of a variable in camel case
    and outputs the corresponding name in snake case. Assume that the
    users input will indeed be in camel case.
    """

    string = input("cameCase: ")

    convert_to_snake_case(string)


def convert_to_snake_case(string: str) -> str:
    """
    Takes a string as input and outputs a string where
    every upper-case char is prefixed with "_" and converted
    to lower case.
    """
    snake = ""
    for i in string:
        if i.isupper():
            snake += "_" + i.lower()
        else:
            snake += i
    print("snake_case: " + snake.lstrip("_"))


if __name__ == "__main__":
    main()
