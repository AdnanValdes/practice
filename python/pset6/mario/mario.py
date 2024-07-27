def main():
    height = get_input()
    draw(height)


def get_input():

    try:
        height = int(input("Height: "))
    except ValueError:
        return get_input()
    if height in range(1, 9):
        return height
    else:
        # If the number is invalid, recurse into same function.
        # Note that this *must* return, so that we can get "height"
        # regardless of recursion level
        return get_input()


def draw(height, row=1):
    # exit condition
    if height == 0:
        exit(0)

    # Actual printing to the terminal
    print(" " * (height - 1) + "#" * row, sep="", end="")
    print("  ", sep="", end="")
    print("#" * row)

    # Set up for next recussion level
    row += 1
    draw(height - 1, row)


if __name__ == "__main__":
    main()
