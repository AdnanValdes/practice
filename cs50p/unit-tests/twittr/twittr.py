VOWELS = ["a", "e", "i", "o", "u"]


def main():
    """
    prompts the user for a str of text and then outputs
    that same text but with all vowels (A, E, I, O, and U)
    omitted, whether inputted in uppercase or lowercase.
    """

    text = input("Input: ")
    print(f"Output: {shorten(text)}")


def is_vowel(s):
    return True if s in VOWELS or s.lower() in VOWELS else False


def shorten(text: str) -> str:
    o = ""
    for i in text:
        if is_vowel(i):
            continue
        else:
            o += i
    return o


if __name__ == "__main__":
    main()
