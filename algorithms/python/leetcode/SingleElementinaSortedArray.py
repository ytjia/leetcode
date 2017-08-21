# -*- coding: utf-8 -*-

# Authors: Y. Jia <ytjia.zju@gmail.com>


"""
Given a sorted array consisting of only integers where every element appears twice except for one
element which appears once. Find this single element that appears only once.

https://leetcode.com/problems/single-element-in-a-sorted-array/description/
"""


class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        the_num = 0
        for num in nums:
            the_num ^= num

        return the_num
