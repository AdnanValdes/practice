import re
import sys

PATTERN = r"\b[Uu][Mm]\b"


def main():
    print(count(input("Text: ")))


def count(s):
    return len(re.findall(PATTERN, s))


if __name__ == "__main__":
    main()
