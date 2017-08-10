#!/usr/bin python
# -*- coding: utf-8 -*-

"""
Given an array of integers, every element appears twice except for one.
Find that single one.
Note:
Your algorithm should have a linear runtime complexity.
Could you implement it without using extra memory?
https://oj.leetcode.com/problems/single-number/
"""

class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        result = 0
        for i in A:
            result ^= i
        return result

if __name__ == '__main__':
    test_case = [
        [1, 1, 3, 4, 4],
        [4, 6, 7, 7, 4]
        ]
    for t in test_case:
        ta = Solution().singleNumber(t)
        print(ta)
