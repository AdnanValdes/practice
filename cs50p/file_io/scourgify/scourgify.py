import sys
import csv
from utils import count_args, is_valid_file

def main():
    if count_args(2) and is_valid_file(sys.argv[1], ["csv"]) and is_valid_file(sys.argv[2], ['csv']):
        parser(sys.argv[1], sys.argv[2])
    else:
        sys.exit(1)

def parser(in_name, out_name):
    with open(in_name, "r") as input, open(out_name, "w") as output:
       reader = csv.DictReader(input)
       writer = csv.DictWriter(output, fieldnames=["first", "last", "house"])
       writer.writeheader()

       for row in reader:
           last, first = row["name"].split(",")
           writer.writerow(
               {"first" : first,
               "last" : last,
               "house" : row["house"]}
           )
    sys.exit(0)


if __name__ == "__main__":
    main()
