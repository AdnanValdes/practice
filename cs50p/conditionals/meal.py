def main():
    """
    Prompts the user for a time and outputs whether it's:
        'breakfast time' - 07:00 to 08:00
        'lunch time'     - 12:00 to 13:00
        'dinner time'    - 18:00 to 19:00

    If it's not time for a meal, there is not output.
    """
    # Convert 24-hour str format to hours in float
    ctime = convert(input("What time is it? "))

    # Check what meal time it is
    mealTime(ctime)


def convert(time):
    """
    Converts a 'str' in 24-hour format to the corresponding number of hours
    as a float. For instance, given a 'time' like "7:30" -> 7.5.
    """
    # Sanitize, split, and convert time to float
    hours, minutes = sanitizeTime(time)

    # Check if minutes > 60
    if minutes > 60:
        print("Enter valid time.")
        quit()

    converted_time = int(hours) + (int(minutes) / 60)

    return converted_time


def sanitizeTime(time: str) -> list:
    hours, minutes = time.strip().split(":")
    return int(hours), int(minutes)


def mealTime(ctime: float) -> str:
    if ctime >= 7 and ctime <= 8:
        print("breakfast time")
    elif ctime >= 12 and ctime <= 13:
        print("lunch time")
    elif ctime >= 18 and ctime <= 19:
        print("dinner time")
    else:
        quit()


if __name__ == "__main__":
    main()
