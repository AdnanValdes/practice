import sys
import random
from pyfiglet import Figlet


def main():
    """
    Expects zero or two command-line arguments:
        Zero if the user would like to output text in a random font.
        Two if the user would like to output text in a specific font,
        in which case the first of the two should be -f or --font,
        and the second of the two should be the name of the font.
    Prompts the user for a str of text.
    Outputs that text in the desired font.

    If the user provides two command-line arguments and the first is
    not -f or --font or the second is not the name of a font, the program
    should exit via sys.exit with an error message.
    """

    args_len = len(sys.argv)
    if args_len < 2:
        prompt()
    elif args_len == 3 and valid_args():
        print(sys.argv[2])
        prompt(font=sys.argv[2])
    else:
        sys.exit("Invalid usage")


def valid_args() -> bool:
    return (sys.argv[1] in ["-f", "--font"]) and (sys.argv[2] in Figlet().getFonts())


def prompt(**f: str) -> None:
    figlet = Figlet()
    text = input("Input: ").strip()

    if f:
        figlet.setFont(font=f)
    else:
        f = random.choice(figlet.getFonts())
        figlet.setFont(font=f)

    print(figlet.renderText(text))


if __name__ == "__main__":
    main()
