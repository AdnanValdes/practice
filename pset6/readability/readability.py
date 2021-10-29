def main():
    text = input("Text: ")
    letters = count_letters(text)
    words = count_words(text)
    sentences = count_sentences(text)
    grade = index(letters, words, sentences)

    if grade > 15:
        print("Grade 16+")
    elif grade < 1:
        print("Before Grade 1")
    else:
        print(f"Grade {grade}")

def count_letters(text):
    '''
    Counts alphanumeric characters; does not include periods or punctuation
    '''
    letters = 0
    for i in text:
        if i.isalpha():
            letters += 1
    return letters

def count_words(text):
    '''
    Counts words by defining a word as anything between spaces.
    Assumes text does not start with a space, nor does it end with a space
    '''
    words = 1
    text = text
    for i in text:
        if i.isspace():
            words += 1
    return words

def count_sentences(text):
    '''
    Checks for punctuation to define sentences.
    Honorifics and the like will create a "sentence"
    '''
    sentences = 0
    for i in text:
        if i in [".", "?", "!"]:
            sentences += 1
    return sentences

def index(letters, words, sentences):
    L = letters / words * 100
    S = sentences / words * 100
    return round(0.0588 * L - 0.296 * S - 15.8)

if __name__ == "__main__":
    main()