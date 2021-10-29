#include <cs50.h>
#include <string.h>
#include <stdio.h>
#include <ctype.h>
#include <stdlib.h>

int cipher(int key);
char encode(char i, int key);

// Get command-line argument and confirm it is numeric only
int main(int argc, string argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./caesar key");
        return 1;
    }

    for (int i = 0, n = strlen(argv[1]); i < n; i++)
    {
        // Using isalpha instead of atoi at each number due to errors at compile time
        if (isalpha(argv[1][i]) != 0)
        {
            printf("Usage: ./caesar key\n");
            return 1;
        }
    }

    int key = atoi(argv[1]);
    cipher(key);
    return 0;
}

// Get_string from user and encrypt
int cipher(int key)
{
    string plaintext = get_string("plaintext:  ");
    printf("ciphertext: ");
    for (int i = 0, n = strlen(plaintext); i < n; i++)
    {
        if (isalpha(plaintext[i]) != 0)
        {
            printf("%c", encode(plaintext[i], key));
        }
        else
        {
            printf("%c", plaintext[i]);
        }
    }
    printf("\n");
    return 0;
}


// Iterate over string rotating characters based on key
// If alphabetical, check case and rotate without changing case
// If punctuation or numerical, keep value
char encode(char i, int key)
{
    int c = 0;
    // If isupper != 0, the character is NOT uppercase.
    if (isupper(i) != 0)
    {
        c = (i + key - 'A') % 26 + 'A';
    }
    else
    {
        c = (i + key - 'a') % 26 + 'a';
    }
    return c;
}