def _checkInt(usr_input):
    if usr_input.isdigit():
        return int(usr_input)
    else:
        print("Must enter digit!")
        quit()


def calculate(usr_input):
    c = 300000000
    E = usr_input * c**2
    print(E)


def main():
    usr_input = input("m: ")
    usr_int = _checkInt(usr_input)

    calculate(usr_int)


main()
