# -*- coding: utf-8 -*-

# Authors: Y. Jia <ytjia.zju@gmail.com>


"""
Given an array of integers and an integer k, you need to find the total number of continuous
subarrays whose sum equals to k.

https://leetcode.com/problems/subarray-sum-equals-k/description/
"""


class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sub_array_cnt = 0
        sum_cnt_dict = dict()
        sum_cnt_dict[0] = 1
        sum = 0
        for num in nums:
            sum += num
            if (sum - k) in sum_cnt_dict:
                sub_array_cnt += sum_cnt_dict[sum - k]
            if sum in sum_cnt_dict:
                sum_cnt_dict[sum] += 1
            else:
                sum_cnt_dict[sum] = 1

        return sub_array_cnt
