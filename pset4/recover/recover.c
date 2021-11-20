#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <stdbool.h>

#define JPEGBLOCK 512

typedef uint8_t BYTE;

bool is_jpeg(BYTE buffer[JPEGBLOCK]);

int main(int argc, char *argv[])
{
	if (argc != 2)
	{
		printf("Usage: ./recover raw");
		return 1;
	}
	FILE *file = fopen(argv[1], "r");
	if (file != NULL)
	{
		BYTE buffer[JPEGBLOCK];
		FILE *img;
		char *filename = malloc(sizeof("###.jpg"));
		int counter = 0;

		// On success, fread() and fwrite() return the number of items read or written. This number equals the number of bytes transferred only when size is 1
		while (fread(&buffer, sizeof(buffer), 1, file) == 1)
		{
			// Check if first 4 bytes are JPEG headers
			if (is_jpeg(buffer))
			{
				if (counter != 0)
				{
					fclose(img);
				}

				sprintf(filename, "%3i.jpg", counter);
				img = fopen(filename, "w");
				counter++;
			}
			if (counter != 0)
			{
				fwrite(&buffer, JPEGBLOCK, 1, img);
			}
		}
		fclose(img);
		fclose(file);
		free(filename);
	}
	else
	{
		printf("Could not read file\n");
		return 1;
	}
	return 0;
}

bool is_jpeg(BYTE buffer[JPEGBLOCK])
{
	if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
	{
		return true;
	}
	return false;
}
