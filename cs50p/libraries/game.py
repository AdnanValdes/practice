import random
import sys


def main():
    level = prompt("Level: ")
    target = random.randrange(1, level)
    guess = prompt("Guess: ")

    while True:
        if guess < target:
            print("Too small!")
        elif guess > target:
            print("Too large!")
        else:
            print("Just right!")
            break

        guess = prompt("Guess: ")


def prompt(prompt: str) -> int:
    while True:
        try:
            number = int(input(prompt))
        except ValueError:
            continue

        except EOFError:
            sys.exit()
        if number > 0:
            return number


if __name__ == "__main__":
    main()
