def main():
    # Get user input
    i = input(
        "What is the Answer to Great Question of Life, the Universe and Everything? "
    )
    # Sanitize input
    i = sanitize(i)

    # Compare to answers
    if isAnswer(i):
        print("Yes")
    else:
        print("No")


def sanitize(i: str):
    return i.strip().lower()


def isAnswer(i: str) -> bool:
    return True if i in ["42", "forty-two", "forty two"] else False


main()
