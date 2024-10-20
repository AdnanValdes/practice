import csv


def main():
    """
    Prompts user for name of a file (i.e. "cat.gif") and return the
    MIME type of that file (i.e. "image/gif")
    """

    # Ask for input
    fname = input("File name: ")

    # Sanitize input (lower case, strip whitespace)
    fname = sanitize(fname)

    # Strip extension from file name
    extension = stripExtension(fname)

    # Initialize supported MIME types dictionary
    mimeDict = {}
    with open("mimes.csv", "r") as mimes:
        reader = csv.reader(mimes, delimiter="\t")

        for row in reader:
            ext = row[0].strip()
            mimeType = row[1]

            mimeDict[ext] = mimeType

    print(mimeDict[extension])


def sanitize(fname: str) -> str:
    return fname.strip().lower()


def stripExtension(fname: str) -> str:
    return "." + fname.partition(".")[2]


main()
