import sys
import inflect
from datetime import datetime, date

p = inflect.engine()


def main():
    dob = input("Date of Birth: ").strip()
    print(seasons(dob))

def convert(time_string):
    date_object = datetime.strptime(time_string, "%Y-%m-%d").date()
    return date_object

def process_seasons(dob):
    time = date.today() - convert(dob)
    return int(time.total_seconds() / 60)

def seasons(dob):
    time = process_seasons(dob)
    minutes = p.number_to_words(time, andword='')
    return f"{minutes.capitalize()} minutes"

if __name__ == "__main__":
    main()
