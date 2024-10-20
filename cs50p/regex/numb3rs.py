import re
import sys

IPV4 = (
    r"^(25[0-5]?|2[0-4]\d|1\d\d|\d\d|\d)"  # Match first octet
    r"(\.(25[0-5]?|2[0-4]\d|1\d\d|\d\d|\d)){2}"  # Match middle octet twice with leading period (.)
    r"\.(25[0-5]?|2[0-4]\d|1\d\d|\d\d|\d)$" # Match last octet
)


def main():
    print(validate(input("IPv4 Address: ")))
    sys.exit(0)


def validate(ipv4: str) -> bool:
    if re.search(IPV4, ipv4):
        return True
    else:
        return False


if __name__ == "__main__":
    main()
