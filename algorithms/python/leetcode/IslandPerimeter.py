# -*- coding: utf-8 -*-

# Authors: Y. Jia <ytjia.zju@gmail.com>

"""
You are given a map in form of a two-dimensional integer grid where 1 represents land and 0
represents water. Grid cells are connected horizontally/vertically (not diagonally). The grid is
completely surrounded by water, and there is exactly one island (i.e., one or more connected land
cells). The island doesn't have "lakes" (water inside that isn't connected to the water around
the island). One cell is a square with side length 1. The grid is rectangular, width and height
don't exceed 100. Determine the perimeter of the island.

https://leetcode.com/problems/island-perimeter/description/
"""


class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        height = len(grid)
        if height == 0:
            return 0
        width = len(grid[0])
        if width == 0:
            return 0
        up_wrapper = list()
        down_wrapper = list()
        for i in range(width + 2):
            up_wrapper.append(0)
            down_wrapper.append(0)
        for i in range(height):
            grid[i].insert(0, 0)
            grid[i].append(0)
        grid.insert(0, up_wrapper)
        grid.append(down_wrapper)

        perimeter = 0
        for i in range(1, height + 1):
            for j in range(1, width + 1):
                if grid[i][j] == 1:
                    if grid[i - 1][j] == 0:
                        perimeter += 1
                    if grid[i + 1][j] == 0:
                        perimeter += 1
                    if grid[i][j - 1] == 0:
                        perimeter += 1
                    if grid[i][j + 1] == 0:
                        perimeter += 1
        return perimeter
