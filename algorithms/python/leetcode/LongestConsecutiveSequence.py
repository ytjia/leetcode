# -*- coding: utf-8 -*-

# Authors: Y. Jia <ytjia.zju@gmail.com>

"""
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

https://leetcode.com/problems/longest-consecutive-sequence/description/
"""


class Segment(object):
    def __init__(self, left, right):
        self.left = left
        self.right = right


class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_set = set(nums)
        lcs = 0
        for num in nums_set:
            if num - 1 not in nums_set:
                c_max = num + 1
                while c_max in nums_set:
                    c_max += 1
                lcs = max(lcs, c_max - num)
        return lcs

    # AC, but a little complex
    def longestConsecutive2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return 0
        lcs = 1
        left_cs_dict = dict()
        right_cs_dict = dict()
        handled_num = set()

        for num in nums:
            if num in handled_num:
                continue
            if num in left_cs_dict and num in right_cs_dict:
                left_seg = left_cs_dict[num]
                right_seg = right_cs_dict[num]
                left_seg.left = right_seg.left
                right_cs_dict[left_seg.right + 1] = left_seg
                left_cs_dict[left_seg.left - 1] = left_seg
                lcs = max(lcs, left_seg.right - left_seg.left + 1)
            elif num in left_cs_dict:
                seg = left_cs_dict[num]
                seg.left -= 1
                left_cs_dict[num - 1] = seg
                lcs = max(lcs, seg.right - seg.left + 1)
            elif num in right_cs_dict:
                seg = right_cs_dict[num]
                seg.right += 1
                right_cs_dict[num + 1] = seg
                lcs = max(lcs, seg.right - seg.left + 1)
            else:
                seg = Segment(num, num)
                right_cs_dict[num + 1] = seg
                left_cs_dict[num - 1] = seg
            handled_num.add(num)

        return lcs
