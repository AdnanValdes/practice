def main():
    user_input = input()
    sentence = convert(user_input)
    print(sentence)


def convert(text):
    return text.replace(":)", "🙂").replace(":(", "🙁")


main()
