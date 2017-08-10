#!/usr/bin python
# -*- coding: utf-8 -*-

"""
Reverse digits of an integer.
Example1: x = 123, return 321
Example2: x = -123, return -321
https://oj.leetcode.com/problems/reverse-integer/
"""

class Solution:
    # @return an integer
    def reverse(self, x):
        if x > 0:
            sign = 1
        else:
            sign = -1
            x = -x
        result = 0
        while x != 0:
            result = result * 10 +  x % 10
            x /= 10
        result = sign * result
        return result

if __name__ == '__main__':
    test_case = [
        123,
        -321,
        10000000000000000000000000003,
        0
        ]
    for test_s in test_case:
        subs = Solution().reverse(test_s)
        print(subs)
