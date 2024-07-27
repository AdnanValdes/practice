from helpers import prompt


def main():
    names = prompt("Name: ")
    print(f"Adieu, adieu, to {render_names(names)}")


def render_names(names: list) -> str:
    if len(names) < 3:
        return " and ".join(names)
    else:
        return ", ".join(names[:-1]) + f", and {names[-1]}"


if __name__ == "__main__":
    main()
