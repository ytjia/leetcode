# -*- coding: utf-8 -*-

# Authors: Y. Jia <ytjia.zju@gmail.com>


"""
Given n non-negative integers representing the histogram's bar height where the width of each bar
is 1, find the area of largest rectangle in the histogram.

https://leetcode.com/problems/largest-rectangle-in-histogram/description/
"""


class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        max_rec = 0
        stack = list()
        i = 0
        while i < len(heights):
            if len(stack) == 0 or heights[stack[-1]] <= heights[i]:
                stack.append(i)
                i += 1
            else:
                cur_top = heights[stack[-1]]
                stack.pop()
                if len(stack) == 0:
                    cur_top_rec_width = i
                else:
                    cur_top_rec_width = i - stack[-1] - 1
                cur_top_rec = cur_top * cur_top_rec_width
                max_rec = max(max_rec, cur_top_rec)

        while len(stack) > 0:
            cur_top = heights[stack[-1]]
            stack.pop()
            if len(stack) == 0:
                cur_top_rec_width = i
            else:
                cur_top_rec_width = i - stack[-1] - 1
            cur_top_rec = cur_top * cur_top_rec_width
            max_rec = max(max_rec, cur_top_rec)

        return max_rec
