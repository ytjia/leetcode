# -*- coding: utf-8 -*-

# Authors: Y. Jia <ytjia.zju@gmail.com>

"""
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive),
prove that at least one duplicate number must exist. Assume that there is only one duplicate
number, find the duplicate one.

https://leetcode.com/problems/find-the-duplicate-number/description/
"""


class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        assert len(nums) > 1
        nums.sort()
        tmp = nums[0]
        for num in nums[1:]:
            if num == tmp:
                return num
            else:
                tmp = num
