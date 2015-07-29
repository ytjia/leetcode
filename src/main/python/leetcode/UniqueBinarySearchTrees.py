#!/usr/bin python       
# -*- coding: utf-8 -*-

"""
Given n, how many structurally unique BST's (binary search trees) 
that store values 1...n?
https://oj.leetcode.com/problems/unique-binary-search-trees/
"""

class Solution:
    # @return an integer
    def numTrees(self, n):
        if n == 0:
            return 1
        else:
            result = i = 0
            while n - i > 0:
                result += self.numTrees(i) * self.numTrees(n-i-1)
                i += 1
            return result
 
if __name__ == '__main__':
    test_case = [
        0,
        1,
        2,
        3,
        4,
        5
        ]
    for t in test_case:
        print Solution().numTrees(t)