# -*- coding: utf-8 -*-

# Authors: Y. Jia <ytjia.zju@gmail.com>

"""
Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it is able to trap after raining.

https://leetcode.com/problems/trapping-rain-water/description/
"""


class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        lens = len(height)
        if lens == 0:
            return 0
        max_height = 0
        max_left = list()
        for i in range(0, lens):
            max_height = max(max_height, height[i])
            max_left.append(max_height)
        max_height = 0
        max_right = list()
        for i in range(lens - 1, -1, -1):
            max_height = max(max_height, height[i])
            max_right.append(max_height)
        max_right.reverse()

        volume = 0
        for i in range(0, lens):
            volume += min(max_left[i], max_right[i]) - height[i]

        return volume

    def trap_slow(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) == 0:
            return 0
        max_height = max(height)
        floor_boundary_list = list()
        for yi in range(0, max_height):
            floor_boundary_list.append(list())
        for xi in range(0, len(height)):
            for yi in (range(0, height[xi])):
                floor_boundary_list[yi].append(xi)

        volume = 0
        for yi in range(0, max_height):
            left = None
            for xi in floor_boundary_list[yi]:
                if left is None:
                    left = xi
                else:
                    volume += xi - left - 1
                    left = xi

        return volume
