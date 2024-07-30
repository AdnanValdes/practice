import re
import sys

FORMAT = (
    r"(?P<shrs>1{0,1}\d):?(?P<smin>[0-5]\d)? (?P<smer>AM|PM)"
    r" to "
    r"(?P<ehrs>1{0,1}\d):?(?P<emin>[0-5]\d)? (?P<emer>AM|PM)"
)


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if m := re.search(FORMAT, s):
        start = manage(m.group("shrs"), m.group("smin"), m.group("smer"))
        end = manage(m.group("ehrs"), m.group("emin"), m.group("emer"))

        return f"{start} to {end}"
    else:
        raise ValueError


def manage(hrs, mins, meridian):
    if mins == None:
        mins = 0
    hrs, mins = int(hrs), int(mins)

    if hrs > 12 or mins >= 60:
        raise ValueError

    if meridian == "AM":
        return f"{hrs:02}:{mins:02}"
    else:
        return f"{hrs+12:02}:{mins:02}"


if __name__ == "__main__":
    main()
