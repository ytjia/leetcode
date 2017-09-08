# -*- coding: utf-8 -*-

# Authors: Y. Jia <ytjia.zju@gmail.com>


"""
The Hamming distance between two integers is the number of positions at which the corresponding
bits are different.

Given two integers x and y, calculate the Hamming distance.

https://leetcode.com/problems/hamming-distance/description/
"""


class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        h_dist = 0

        while x > 0 or y > 0:
            if x == 0:
                bit_x = 0
            else:
                bit_x = x % 2
                x = x >> 1
            if y == 0:
                bit_y = 0
            else:
                bit_y = y % 2
                y = y >> 1
            h_dist += bit_x ^ bit_y

        return h_dist
