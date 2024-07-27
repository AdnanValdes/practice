import sys


def main():
    len_argv = len(sys.argv)
    if len_argv < 2:
        sys.exit("Too few command-line arguments")
    elif len_argv > 2:
        sys.exit("Too many command-line arguments")

    file = sys.argv[1]
    if is_valid_file(file):
        print(parse_file(file))
    sys.exit(0)


def is_valid_file(filename: str) -> bool:
    try:
        name, ext = filename.split(".")
        if ext not in ["py", "txt", "json", "csv"]:
            raise ValueError
    except ValueError:
        sys.exit("Not a valid file")

    return True


def parse_file(filename: str) -> int:
    count = 0
    try:
        with open(filename) as file:
            for line in file:
                if not count_line(line):
                    count += 1
    except FileNotFoundError:
        sys.exit("File does not exist")
    return count


def count_line(line):
    line = line.lstrip()
    return line.startswith("#") or line == "" or line.isspace()


if __name__ == "__main__":
    main()
