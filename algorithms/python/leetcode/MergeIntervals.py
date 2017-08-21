# -*- coding: utf-8 -*-

# Authors: Y. Jia <ytjia.zju@gmail.com>

"""
Given a collection of intervals, merge all overlapping intervals.

https://leetcode.com/problems/merge-intervals/description/
"""


# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __eq__(self, other):
        return self.start == other.start and self.end == other.end


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        lens = len(intervals)
        if lens <= 1:
            return intervals
        merged_intervals = list()
        intervals.sort(key=lambda interval: interval.start)
        i = 0
        j = i + 1
        while j < lens:
            if intervals[i].end >= intervals[j].start:
                intervals[i].end = max(intervals[i].end, intervals[j].end)
                j += 1
            else:
                merged_intervals.append(intervals[i])
                i = j
                j = i + 1
        merged_intervals.append(intervals[i])

        return merged_intervals
