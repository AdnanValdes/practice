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

            // Need to divide by float here because all RGB values are ints
            // Any division by another int will return an int
            // This leads to truncated values
            average = round(average / 3.0);
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
    // Create temporary array to store values
    for (int i=0; i<height; i++)
    {
        for (int j=0; j < width / 2; j++)
        {
            RGBTRIPLE tmp = image[i][j];
            image[i][j] = image[i][width - (j + 1)];
            image[i][width - (j + 1)] = tmp;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    // Box blur: computer value of each pixel by taking the average for all values within a column and row of the pixel

    // Create a copy of the image
    RGBTRIPLE tmp[height][width];
    RGBTRIPLE colors;

    for (int i=0; i < height; i++)
    {
        for (int j=0; j<width;j++)
        {
            tmp[i][j] = image[i][j];
        }
    }

    // Iterate over rows and columns to get each pixel
    for (int i=0; i<height; i++)
    {
        for (int j=0; j < width; j++)
        {
            colors.rgbtBlue = 0;
            colors.rgbtGreen = 0;
            colors.rgbtRed = 0;

            int totalPixels = 0;

            // Pretend we can only look at a smaller array of -1 to +1 from current pixel
            for (int k=-1; k < 2; k++)
            {
                for (int l=-1; l < 2; l++)
                {
                    // Check for corners and edges
                    int horizontal = i + k;
                    int vertical = j + l;
                    if ((horizontal >= 0 && horizontal < height) && (vertical >=0 && vertical < width))
                    {
                        colors.rgbtRed += tmp[horizontal][vertical].rgbtRed;
                        colors.rgbtBlue += tmp[horizontal][vertical].rgbtBlue;
                        colors.rgbtGreen += tmp[horizontal][vertical].rgbtGreen;
                        totalPixels++;
                    }
                }
            }

            image[i][j].rgbtGreen = round(colors.rgbtGreen / totalPixels);
            image[i][j].rgbtBlue = round(colors.rgbtBlue / totalPixels);
            image[i][j].rgbtRed = round(colors.rgbtRed / totalPixels);
        }
    }
    return;
}
