# -*- coding: utf-8 -*-

# Authors: Y. Jia <ytjia.zju@gmail.com>


"""
Given an integer array, you need to find one continuous subarray that if you only sort this
subarray in ascending order, then the whole array will be sorted in ascending order, too.

You need to find the shortest such subarray and output its length.

https://leetcode.com/problems/shortest-unsorted-continuous-subarray/description/
"""


class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) <= 1:
            return 0
        chaos_b = 0
        chaos_e = 0

        max = nums[0]
        for i in range(1, len(nums)):
            if nums[i] >= max:
                max = nums[i]
            else:
                chaos_e = i

        min = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] <= min:
                min = nums[i]
            else:
                chaos_b = i

        if chaos_b == chaos_e:
            return 0
        else:
            return chaos_e - chaos_b + 1
