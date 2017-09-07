# -*- coding: utf-8 -*-

# Authors: Y. Jia <ytjia.zju@gmail.com>

"""
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and
return its area.

https://leetcode.com/problems/maximal-square/description/
"""


class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        max_side_length = 0
        if matrix is None:
            return max_side_length
        n_row = len(matrix)
        if n_row == 0:
            return max_side_length
        n_col = len(matrix[0])

        dp = list()
        for r in range(n_row):
            dp.append(list())
            for c in range(n_col):
                dp[r].append(0)

        for r in range(n_row):
            dp[r][0] = int(matrix[r][0])
            max_side_length = max(dp[r][0], max_side_length)
        for c in range(n_col):
            dp[0][c] = int(matrix[0][c])
            max_side_length = max(dp[0][c], max_side_length)

        for r in range(1, n_row):
            for c in range(1, n_col):
                if matrix[r][c] == '1':
                    dp[r][c] = min(dp[r - 1][c - 1], dp[r - 1][c], dp[r][c - 1]) + 1
                    max_side_length = max(dp[r][c], max_side_length)
                else:
                    dp[r][c] = 0

        return max_side_length * max_side_length
