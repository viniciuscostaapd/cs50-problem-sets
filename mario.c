#include <cs50.h>
#include <stdio.h>

void print_row(int spaces, int bricks);

int main(void)
{
    // Prompt the user for the pyramid's height
    int n;
    do
    {
        n = get_int("Height: ");
    }
    while ((n < 1) || (n > 8));

    // Print a pyramid of that height
    for (int i = 0; i < n; i++)
    {
        // Print row of bricks
        print_row(n, i);
    }
}

void print_row(int spaces, int bricks)
{
    // Print spaces
    for (int j = (spaces - bricks) - 1; j > 0; j--)
    {
        printf(" ");
    }

    // Print left side bricks
    for (int k = 0; k < (bricks + 1); k++)
    {
        printf("#");
    }

    // Print the gap
    printf("  ");

    // Print right side bricks
    for (int k = 0; k < (bricks + 1); k++)
    {
        printf("#");
    }

    printf("\n");
}
