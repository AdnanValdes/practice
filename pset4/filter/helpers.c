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
                average = (average + *(&image[i][j].rgbtBlue + k));
            }

            average = round(average / 3);
            for (int k=0; k < count; k++)
            {
                *(&image[i][j].rgbtBlue + k) = average;
            }

        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    // Each pixel must be converted to sepia equivalent
    // A sepia formula must be used for this
    // Values must be rounded
    // If values are close to 255, the result might be > 255. Must set 255 as max.
    // loop through rows
    for (int i=0; i<height; i++)
    {
        // loop through pixels in row
        for (int j=0; j<width; j++)
        {
            int sepiaRed = round(.393 * image[i][j].rgbtRed + .769 * image[i][j].rgbtGreen + .189 * image[i][j].rgbtBlue);

            int sepiaGreen = round(.349 * image[i][j].rgbtRed + .686 * image[i][j].rgbtGreen + .168 * image[i][j].rgbtBlue);

            int sepiaBlue = round(.272 * image[i][j].rgbtRed + .534 * image[i][j].rgbtGreen + .131 * image[i][j].rgbtBlue);

            if (sepiaRed > 255)
            {
                sepiaRed = 255;
            }

            if (sepiaGreen > 255)
            {
                sepiaGreen = 255;
            }
            if (sepiaBlue > 255)
            {
                sepiaBlue = 255;
            }

            image[i][j].rgbtRed = sepiaRed;
            image[i][j].rgbtBlue = sepiaBlue;
            image[i][j].rgbtGreen = sepiaGreen;
        }
    }
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
