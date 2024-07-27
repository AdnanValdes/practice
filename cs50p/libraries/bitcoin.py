import requests
import json
import sys


def main():
    args_len = len(sys.argv)
    if args_len != 2:
        sys.exit("Missing command-line argument")
    try:
        num = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    make_request(num)


def make_request(num: float) -> None:
    try:
        r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    except requests.RequestException:
        sys.exit("The operation could not be completed")

    try:
        bitcoin_value = r.json()["bpi"]["USD"]["rate_float"]
    except KeyError:
        sys.exit("Something went wrong, try again.")
    print(f"{num * bitcoin_value:,.4f}")


if __name__ == "__main__":
    main()
