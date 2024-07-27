def main():
    # Ask for input
    i = input("Greeting: ")
    # Sanitize input
    i = sanitize(i)

    # Does the greeting start with "hello"?
    if startsHello(i):
        print("$0")
        quit()
    # Does the greeting start with an "h"?
    elif startsH(i):
        print("$20")
        quit()
    else:
        print("$100")


def sanitize(i: str) -> bool:
    return i.strip().lower()


def startsHello(i: str) -> bool:
    return i.startswith("hello")


def startsH(i: str) -> bool:
    return i.startswith("h")


main()
