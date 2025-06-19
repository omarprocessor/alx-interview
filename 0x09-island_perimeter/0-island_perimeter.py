#!/usr/bin/python3
"""
This module defines the island_perimeter function
which calculates the perimeter of an island in a grid.
The grid contains 0s (water) and 1s (land).
"""


def island_perimeter(grid):
    """
    Calculates the perimeter of the island in the grid.

    Args:
        grid (list of list of int): 2D grid representing the island

    Returns:
        int: perimeter of the island
    """
    perimeter = 0
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == 1:
                perimeter += 4
                if y > 0 and grid[y - 1][x] == 1:
                    perimeter -= 2
                if x > 0 and grid[y][x - 1] == 1:
                    perimeter -= 2
    return (perimeter)
