# -*- coding: utf-8 -*-

# Authors: Y. Jia <ytjia.zju@gmail.com>

"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach
the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

https://leetcode.com/problems/unique-paths/description/
"""


class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # C^m_m+n
        num = 1
        den = 1
        for i in range(m + n - 2, n - 1, -1):
            num *= i
        for i in range(m - 1, 0, -1):
            den *= i
        return num / den
