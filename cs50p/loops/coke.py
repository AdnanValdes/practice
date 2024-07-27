COKE = 50
DENOMINATIONS = [25, 10, 5]


def main():
    """
    A machine that sells bottles of coke charges 50 cents
    and only accepts coins in these denominations:
        25 cents
        10 cents
        5  cents

    Prompts the user to insert a coin, one at a time, each
    time informing the user of the amount due. Once the user
    has inputted at least 50 cents, output how many cents in
    change the user is owed.

    Assume the user will only input integers and ignore any
    integers that isn't an accepted denomination
    """
    # The world starts with 50 due and 0 given
    insert_coin(COKE, 0)


def insert_coin(due, given):
    """
    Print amount due, then accept coins in given DENOMINATIONS
    """
    # Print Amount Due
    print("Amount due: ", COKE - given)

    # Ask for coin
    coin = int(input("Insert coin: "))
    if coin not in DENOMINATIONS:
        insert_coin(due, given)

    # Check if payment is sufficient
    if coin + given < COKE:
        # Subtract coin from amount due
        insert_coin(due, given + coin)
    else:
        # Print amount owed
        print("Change owed:", abs(COKE - coin - given))


if __name__ == "__main__":
    main()
