import re
import sys

IPV4 = r"^(25[0-5]?|2[0-4]\d|1\d\d|\d\d|\d)(\.(25[0-5]?|2[0-4]\d|1\d\d|\d\d|\d)){2}\.(25[0-5]?|2[0-4]\d|1\d\d|\d\d|\d)$"

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ipv4: str) -> bool:
    if re.search(IPV4, ipv4):
        return True
    else:
        return False


if __name__ == "__main__":
    main()
