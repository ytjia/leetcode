# -*- coding: utf-8 -*-

# Authors: Y. Jia <ytjia.zju@gmail.com>

"""
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all
unique triplets in the array which gives the sum of zero.

https://leetcode.com/problems/3sum/description/
"""


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        triplets_list = list()
        if nums is None or len(nums) < 3:
            return triplets_list
        nums.sort()

        i = 0
        pre_i_value = None
        while i < len(nums) - 2:
            if nums[i] == pre_i_value:
                i += 1
                continue
            else:
                pre_i_value = nums[i]
            l, j = i + 1, len(nums) - 1
            while l < j:
                s = nums[i] + nums[j] + nums[l]
                if s < 0:
                    l += 1
                elif s > 0:
                    j -= 1
                else:
                    triplets_list.append([nums[i], nums[j], nums[l]])
                    while l < j and nums[l] == nums[l + 1]:
                        l += 1
                    while l < j and nums[j] == nums[j - 1]:
                        j -= 1
                    l += 1
                    j -= 1
            i += 1
        return triplets_list
