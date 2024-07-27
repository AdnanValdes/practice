VWLS = ["a", "e", "i", "o", "u"]


def main():
    """
    prompts the user for a str of text and then outputs
    that same text but with all vowels (A, E, I, O, and U)
    omitted, whether inputted in uppercase or lowercase.
    """

    s = input("Input: ")
    o = ""
    for i in s:
        if is_vowel(i):
            continue
        else:
            o += i
    print("Output:", o)


def is_vowel(s):
    return True if s in VWLS or s.lower() in VWLS else False


if __name__ == "__main__":
    main()
