def main():

    # Ask how many cents the customer is owed
    cents = get_cents()

    # Calculate quarters to give the customer
    quarters = calculate_quarters(cents)
    cents = cents - quarters * 25

    # Calculate dimes to give the customer
    dimes = calculate_dimes(cents)
    cents = cents - dimes * 10

    # Calculate nickels to give the customer
    nickels = calculate_nickels(cents)
    cents = cents - nickels * 5

    # Calculate pennies to give the customer
    pennies = calculate_pennies(cents)
    cents= cents - pennies * 1

    # Sum coins
    coins = quarters + dimes + nickels + pennies

    print(int(coins))

def get_cents():

    dollars = -1
    while dollars < 0:
        try:
            dollars = float(input("Change owed: "))
        except ValueError:
            continue

    cents = dollars * 100
    return cents

def calculate_quarters(cents):
    quarters = cents / 25
    return int(quarters)

def calculate_dimes(cents):
    dimes = cents / 10
    return int(dimes)

def calculate_nickels(cents):
    nickels = cents / 5
    return int(nickels)

def calculate_pennies(cents):
    pennies = cents / 1
    return int(pennies)

if __name__ == "__main__":
    main()