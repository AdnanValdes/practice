import sys

def main():
    pass

def count_args(count):
    len_argv = len(sys.argv) - 1
    if len_argv < count:
        sys.exit("Too few command-line arguments")
    elif len_argv > count:
        sys.exit("Too many command-line arguments")

    return True

def is_valid_file(filename: str, extension: list) -> bool:
    try:
        name, ext = filename.split(".")
        if ext not in extension:
            raise ValueError
    except ValueError:
        sys.exit("Not a valid file")

    return True
if __name__ == "__main__":

    main()
