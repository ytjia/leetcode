# -*- coding: utf-8 -*-

# Authors: Y. Jia <ytjia.zju@gmail.com>


"""
Given a collection of distinct numbers, return all possible permutations.

https://leetcode.com/problems/permutations/description/
"""

import copy


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 1:
            return [nums]

        result = list()
        for num in nums:
            cnums = copy.copy(nums)
            cnums.remove(num)
            for sub_permute in self.permute(cnums):
                result.append([num] + sub_permute)

        return result
