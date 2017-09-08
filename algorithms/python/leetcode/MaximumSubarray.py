# -*- coding: utf-8 -*-

# Authors: Y. Jia <ytjia.zju@gmail.com>

"""
Find the contiguous subarray within an array (containing at least one number) which has the
largest sum.

https://leetcode.com/problems/maximum-subarray/description/
"""


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return None

        max_sum = nums[0]
        cur_sum = nums[0]

        for num in nums[1:]:
            if cur_sum <= 0:
                cur_sum = num
            else:
                cur_sum += num

            max_sum = max(max_sum, cur_sum)

        return max_sum
