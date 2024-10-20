def main():
    pass


def prompt(prompt: str) -> list:
    """
    Prompts for items until control-d is pressed.
    Returns a list of items.
    """
    items = []
    while True:
        try:
            item = input(prompt).strip()
            items.append(item)
        except EOFError:
            print("")
            break
    return items


if __name__ == "__main__":
    main()
