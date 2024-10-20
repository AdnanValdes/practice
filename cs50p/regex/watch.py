import re
import sys

MATCH = r"https?://(?:www.)?youtube.com/embed/(\w+)"


def main():
    print(parse(input("HTML: ")))


def parse(s: str) -> None | str:
    if match := re.search(MATCH, s, re.IGNORECASE):
        return f"https://youtu.be/{match.group(1)}"
    else:
        return None


if __name__ == "__main__":
    main()
