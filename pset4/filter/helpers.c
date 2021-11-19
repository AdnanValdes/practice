#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    // Set ligher colors to lighter rgb (RGB will all be the same, relatively high values)
    // We can do this by taking the average for each triple and setting it for all three (might need to be rounded)
    // Must loop through each row, and within each row, loop through each pixel

    // loop through rows
    for (int i=0; i<height; i++)
    {
        // loop through pixels in row
        for (int j=0; j<width; j++)
        {
            // loop through elements in struct
            // see https://stackoverflow.com/questions/1784782/is-there-any-way-to-loop-through-a-struct-with-elements-of-different-types-in-c
            int count = sizeof(RGBTRIPLE) / sizeof(BYTE);
            int average = 0;

            for (int k=0; k < count; k++)
            {
                average = (average + *(&image[i][j].rgbtBlue + k) );
            }

            average = round(average / 3);
            for (int k=0; k < count; k++)
            {
                *(&image[i][j].rgbtBlue + k) = average;
            }

        }
    }

    // loop through columns

    // calculate average

    // set average for all
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    return;
}
