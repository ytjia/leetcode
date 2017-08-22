# -*- coding: utf-8 -*-

# Authors: Y. Jia <ytjia.zju@gmail.com>

"""
Given an unsorted array of integers, find the length of longest increasing subsequence.

https://leetcode.com/problems/longest-increasing-subsequence/description/
"""


class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        lens_value_list = list()
        lens_value_list.append(nums[0])

        for i in range(1, len(nums)):
            index_just_less = self.binary_search_just_less(lens_value_list, nums[i])
            if index_just_less + 1 > len(lens_value_list) - 1:
                lens_value_list.append(nums[i])
            else:
                if lens_value_list[index_just_less + 1] > nums[i]:
                    lens_value_list[index_just_less + 1] = nums[i]

        return len(lens_value_list)

    def binary_search_just_less(self, arr, target, begin=None, end=None):
        """
        找到arr中小于等于target的最大元素位置
        :param arr:
        :param target:
        :param begin:
        :param end:
        :return:
        """
        if begin is None:
            begin = 0
        if end is None:
            end = len(arr) - 1
        if end < begin or end < 0:
            return begin - 1
        elif end == begin:
            if arr[end] < target:
                return end
            else:
                return end - 1

        mid = begin + (end - begin) / 2
        if arr[mid] < target:
            return self.binary_search_just_less(arr, target, mid + 1, end)
        else:
            return self.binary_search_just_less(arr, target, begin, mid - 1)
