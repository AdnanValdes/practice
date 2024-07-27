MONTHS = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]


def main():
    """
    implement a program that prompts the user for a date, anno Domini,
    in month-day-year order, formatted like 9/8/1636 or September 8, 1636,
    wherein the month in the latter might be any of the values in the MONTHS
    list.

    Assume that every month has no more than 31 days;
    no need to validate whether a month has 28, 29, 30, or 31 days.
    """
    date = input("Date: ").replace(",", "").strip()

    if "/" in date:
        month_day_year(date)
    else:
        longdate(date)


def month_day_year(date: str) -> None:
    try:
        mm, dd, yy = map(int, date.split("/"))
        if validate_month_day(dd, mm):
            print(f"{yy}-{mm:02}-{dd:02}")
        else:
            main()
    except ValueError:
        main()


def longdate(date: str) -> None:
    try:
        mm, dd, yy = date.split(" ")
        dd, yy = map(int, [dd, yy])
        if validate_month_day(dd):
            print(f"{yy}-{MONTHS.index(mm) + 1:02}-{dd:02}")
        else:
            main()
    except ValueError:
        main()


def validate_month_day(d: int, m: int = 0) -> bool:
    return (m < 13) and (d < 32)


if __name__ == "__main__":
    main()
