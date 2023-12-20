#!/usr/bin/python3
""" Returns island perimeter """


def island_perimeter(grid):
    """ Checks perimeter """
    perimeter = 0

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 1:
                # Check left
                if col == 0 or grid[row][col - 1] == 0:
                    perimeter += 1
                # Check right
                if col == len(grid[0]) - 1 or grid[row][col + 1] == 0:
                    perimeter += 1
                # Check up
                if row == 0 or grid[row - 1][col] == 0:
                    perimeter += 1
                # Check down
                if row == len(grid) - 1 or grid[row + 1][col] == 0:
                    perimeter += 1

    return perimeter
