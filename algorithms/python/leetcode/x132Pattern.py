# -*- coding: utf-8 -*-

# Authors: Y. Jia <ytjia.zju@gmail.com>

"""
Given a sequence of n integers a1, a2, ..., an, a 132 pattern is a subsequence ai, aj, ak such that
i < j < k and ai < ak < aj. Design an algorithm that takes a list of n numbers as input and checks
whether there is a 132 pattern in the list.

Note: n will be less than 15,000.

https://leetcode.com/problems/132-pattern/description/
"""


class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        lens = len(nums)
        if lens < 3:
            return False
        min_list = list()
        min_list.append(nums[0])
        for i in range(1, lens):
            min_list.append(min(min_list[i - 1], nums[i]))
        stack = list()
        for j in range(lens - 1, 0, -1):
            if nums[j] > min_list[j]:
                while len(stack) > 0 and stack[-1] <= min_list[j]:
                    stack.pop()
                if len(stack) > 0 and stack[-1] < nums[j]:
                    return True
                stack.append(nums[j])
        return False
