# -*- coding: utf-8 -*-

# Authors: Y. Jia <ytjia.zju@gmail.com>


"""
You are a professional robber planning to rob houses along a street. Each house has a certain
amount of money stashed, the only constraint stopping you from robbing each of them is that
adjacent houses have security system connected and it will automatically contact the police if
two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine
the maximum amount of money you can rob tonight without alerting the police.

https://leetcode.com/problems/house-robber/description/
"""


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None:
            return 0
        num_cnt = len(nums)
        if num_cnt == 0:
            return 0
        elif num_cnt == 1:
            return nums[0]
        elif num_cnt == 2:
            return max(nums[0], nums[1])

        max_m = list()
        max_m.append(nums[0])
        max_m.append(max(nums[0], nums[1]))
        for i in range(2, num_cnt):
            max_m.append(max(nums[i] + max_m[i - 2], max_m[i - 1]))

        return max_m[-1]
