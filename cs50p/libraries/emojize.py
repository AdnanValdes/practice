import emoji


def main():
    """
    prompts the user for a str in English and then outputs the “emojized”
    version of that str, converting any codes (or aliases) therein to their
    corresponding emoji.
    """
    emo = input("Input: ").lower().strip()
    print(emoji.emojize(emo))


if __name__ == "__main__":
    main()
