def main() -> None:
    """
    implement a program that prompts the user for items, one per line,
    until the user inputs control-d (which is a common way of ending one’s
    input to a program). Then output the user’s grocery list in all uppercase,
    sorted alphabetically by item,  prefixing each line with the number of
    times the user inputted that item. No need to pluralize the items. Treat
    the user’s input case-insensitively.
    """
    items = {}
    add(items)


def add(items: dict) -> dict | None:
    """
    Until the user inputs control-d keep prompting for new items. Add each
    item to the items dict in upper-case. After control-d, print grocery list
    """
    try:
        item = input().upper()
        if item in items:
            items[item] += 1
        else:
            items[item] = 1
        add(items)
    except EOFError:
        for i in sorted(items):
            print(items[i], i)


if __name__ == "__main__":
    main()
