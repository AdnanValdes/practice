import random
import sys


def main():
    """
    Prompts the user for a level,
    If the user does not input 1, 2, or 3, the program prompts again.
    Randomly generates ten (10) math problems formatted as X + Y =,
    wherein each of X and Y is a non-negative integer with
    digits. No need to support operations other than addition (+).
    Prompts the user to solve each of those problems. If an answer is
    not correct (or not even a number), the program should output EEE
    and prompt the user again, allowing the user up to three tries in
    total for that problem. If the user has still not answered correctly
    after three tries, the program should output the correct answer.
    The program should ultimately output the user’s score: the number
    of correct answers out of 10.
    """
    lvl = get_level()
    generate_integer(lvl)

    score = 0
    for _ in range(10):
        x, y = generate_integer(lvl), generate_integer(lvl)
        result = x + y

        for i in range(3):
            answer = prompt(f"{x} + {y} = ")
            try:
                answer = int(answer)
            except ValueError:
                print("EEE")
            else:
                if answer != result:
                    print("EEE")
                else:
                    score += 1
                    break
            if i >= 2:
                print(f"{x} + {y} = {result}")

    print(f"Score: {score}")
    sys.exit(0)


def get_level() -> int:
    """
    Prompts the user for a level and returns `1`, `2`, or `3`.
    """
    level = 0
    while level not in [1, 2, 3]:
        try:
            level = int(prompt("Level: "))
        except ValueError:
            continue
    return level


def generate_integer(level: int):
    """
    returns a randomly generated not-negative integer
    with 'level' digits.
    """
    if level not in [1, 2, 3]:
        raise ValueError

    return random.randrange(1, 10**level)


def prompt(prompt: str) -> str:
    while True:
        try:
            value = input(prompt)
        except EOFError:
            sys.exit()
        return value


if __name__ == "__main__":
    main()
