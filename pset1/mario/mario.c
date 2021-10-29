#include <stdio.h>
#include <cs50.h>

void print_line(int height, int rows);

int main(void)
{
    int height = 0;
    do
    {
         height = get_int("Height: ");
    }
    while (height < 1 || height > 8);

    for (int rows = 1; rows < height; rows++)
    {
        print_line(height, rows);
        printf("\n");
    }

    printf("%.*s\n", height, "########");
}



void print_line(int height, int rows)
{

    for (int spaces = height - rows; spaces > 0; spaces--)
    {
        printf(" ");
    }
    for (int hashes = 1; hashes <= rows; hashes++)
    {
        printf("#");
    }
}