RAW_FRUITS = {
    "apple": 130,
    "avocado": 50,
    "banana": 110,
    "cantaloupe": 50,
    "grapefruit": 60,
    "grapes": 90,
    "honeydew melon": 50,
    "kiwifruit": 90,
    "lemon": 15,
    "lime": 20,
    "nectarine": 60,
    "orange": 80,
    "peach": 60,
    "pear": 100,
    "pineapple": 50,
    "plums": 70,
    "strawberries": 50,
    "sweet cherries": 100,
    "tangerine": 50,
    "watermelon": 80,
}


def main():
    """
    User inputs a fruit (case-insensitively) and
    then outputs the number of calories in one portion
    of that fruit.
    """
    fruit = input("Item: ").lower().strip()

    if fruit in RAW_FRUITS:
        print("Calories: ", RAW_FRUITS[fruit])


if __name__ == "__main__":
    main()
