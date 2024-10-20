MENU = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00,
}


def main():
    """
    enables a user to place an order, prompting them for items, one per line,
    until the user inputs control-d (which is a common way of ending one’s input
    to a program).  After each inputted item, display the total cost of all items
    inputted thus far, prefixed with a dollar sign ($) and formatted to two decimal
    places.
    """
    total = 0.00
    order(total)


def order(total: float) -> None:
    try:
        item = input("Item: ").title()
        total += MENU[item]
        print(f"Total: ${total:.2f}")
        order(total)
    except EOFError:
        pass
    except KeyError:
        order(total)


if __name__ == "__main__":
    main()
