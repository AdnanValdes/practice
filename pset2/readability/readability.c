#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <math.h>


int count_letters(string text);
int count_words(string text);
int count_sentences(string text);
int index(int letters, int words, int sentences);

int main(void)
{
    string text = get_string("Text: ");
    int letters = count_letters(text);
    int words = count_words(text);
    int sentences = count_sentences(text);

    int grade = index(letters, words, sentences);

    if (grade > 15)
    {
        printf("Grade 16+\n");
    }
    else if (grade < 1)
    {
        printf("Before Grade 1\n");
    }
    else
    {
        printf("Grade %i\n", grade);
    }
}

// Letters are considered to be alphanumeric characters. Periods and other punctuation do not count.
int count_letters(string text)
{
    int letters = 0;
    for (int i = 0, n = strlen(text); i < n; i++)
    {
        if (isalpha(text[i]) != 0)
        {
            letters++;
        }
    }
    return letters;
}

// Defines a word based on a space. Assumes a text does not start with a space, nor does it end with a space.
int count_words(string text)
{
    int words = 0;
    for (int i = 0, n = strlen(text); i < n; i++)
    {
        if (isspace(text[i]) != 0)
        {
            words++;
        }
    }
    return words + 1;
}

// Checks for punctuation to define a sentence. Honorifics and the like will create a sentence.
int count_sentences(string text)
{
    int sentences = 0;
    for (int i = 0, n = strlen(text); i < n; i++)
    {
        if (text[i] == '.' || text[i] == '?' || text[i] == '!')
        {
            sentences++;
        }
    }
    return sentences;
}

// Uses Coleman-Liau index to output a US grade level for a text
int index(int letters, int words, int sentences)
{
    // Casts ints to floats for accurate divison results
    float L = (float)letters / (float)words * 100;
    float S = (float)sentences / (float)words * 100;

    return (int)round((0.0588 * L - 0.296 * S - 15.8));
}