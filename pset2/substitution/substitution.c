#include <cs50.h>
#include <string.h>
#include <stdio.h>
#include <ctype.h>
#include <stdlib.h>


string strupr(string text);
string strlwr(string text);
// Get command-line argument and confirm it is numeric only
int main(int argc, string argv[])
{
    // Input validation

    // Check for argv count
    if (argc != 2)
    {
        printf("Usage: ./caesar key");
        return 1;
    }

    // Check for key lenght == 26 chars
    int key_len = strlen(argv[1]);
    if (key_len != 26)
    {
        printf("Key must contain 26 characters.\n");
        return 1;
    }

    // Check that all characters are alphabetical
    for (int i = 0; i < key_len; i++)
    {
        if (isalpha(argv[1][i]) == 0)
        {
            printf("Usage: ./caesar key\n");
            return 1;
        }
    }

    string key = strupr(argv[1]);

    // Check that there are no repeated characters
    // Summing all upper case letters == 2015

    int sum, j;
    for (sum=0, j=0; j < key_len; j++)
    {
        sum += key[j];
    }
    if (sum != 2015)
    {
        printf("Key must not contain repeated characters.\n");
        return 1;
    }

    // Get input and encipher

    string plaintext = get_string("plaintext: ");

    printf("ciphertext: ");
    for (int i = 0, n = strlen(plaintext); i < n; i++)
    {
        if (isalpha(plaintext[i]) == 0)
        {
            plaintext[i] = plaintext[i];
        }
        else if (isupper(plaintext[i]) != 0)
        {
            int x = plaintext[i] - 'A';
            plaintext[i] = *strupr(&key[x]);
        }
        else
        {
            int x = plaintext[i] - 'a';
            plaintext[i] = *strlwr(&key[x]);
        }
        printf("%c", plaintext[i]);
    }
    printf("\n");
}

string strupr(string text)
{
    for (int i = 0; text[i] != '\0'; i++)
    {
        if (text[i] >= 'a' && text[i] <= 'z')
        {
            text[i] = toupper(text[i]);
        }
    }
    return text;
}

string strlwr(string text)
{
    for (int i = 0; text[i] != '\0'; i++)
    {
        if (text[i] >= 'A' && text[i] <= 'Z')
        {
            text[i] = tolower(text[i]);
        }
    }
    return text;
}