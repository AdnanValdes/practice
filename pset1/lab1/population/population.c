#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // TODO: Prompt for start size
    int n_start = 0;
    int n_end = 0;

    do
    {
        n_start = get_int("Starting population: ");
    }
    while (n_start < 9);

    // TODO: Prompt for end size
    do
    {
        n_end = get_int("End population: ");
    }
    while (n_end < n_start);

    // TODO: Calculate number of years until we reach threshold
    int years = 0;
    do
    {
        if (n_start == n_end)
            break;
            
        int new_llamas = n_start / 3;
        int dead_llamas = n_start / 4;
        n_start = n_start + new_llamas - dead_llamas;
        years++;
    }
    while (n_start < n_end);

    // TODO: Print number of years
    printf("Years: %i\n", years);
}