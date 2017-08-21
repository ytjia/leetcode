# -*- coding: utf-8 -*-

# Authors: Y. Jia <ytjia.zju@gmail.com>

"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
You are given a target value to search. If found in the array return its index, otherwise return -1.
You may assume no duplicate exists in the array.

https://leetcode.com/problems/search-in-rotated-sorted-array/description/
"""


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        end = len(nums) - 1
        if end < 0:
            return -1
        return self.search_with_rotated(nums, 0, end, target)

    def search_with_rotated(self, nums, begin, end, target):
        """

        :param nums:
        :param begin:
        :param end:
        :param target:
        :return:
        """
        if end < begin:
            return -1
        if end == begin:
            if nums[end] == target:
                return end
            else:
                return -1
        mid = begin + (end - begin) / 2
        # pivot in left
        if nums[mid] == target:
            return mid
        if nums[mid] <= nums[end] <= nums[begin]:
            if nums[mid] < target <= nums[end]:
                return self.search_with_rotated(nums, mid + 1, end, target)
            else:
                return self.search_with_rotated(nums, begin, mid - 1, target)
        # pivot in right
        elif nums[end] <= nums[begin] <= nums[mid]:
            if nums[begin] <= target < nums[mid]:
                return self.search_with_rotated(nums, begin, mid - 1, target)
            else:
                return self.search_with_rotated(nums, mid + 1, end, target)
        # no pivot
        else:
            if target > nums[mid]:
                return self.search_with_rotated(nums, mid + 1, end, target)
            else:
                return self.search_with_rotated(nums, begin, mid - 1, target)
