def main():
    i = input("Greeting: ").lower().strip()
    print(f"${value(i)}")


def value(greeting: str) -> int:
    if greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
