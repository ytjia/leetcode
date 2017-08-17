# -*- coding: utf-8 -*-

# Authors: Y. Jia <ytjia.zju@gmail.com>

"""
Given a string, find the length of the longest substring without repeating characters.

https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
"""


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_length = 0
        cur_substr = list()
        for i in range(0, len(s)):
            if s[i] in cur_substr:
                max_length = max(max_length, len(cur_substr))
                cur_substr = cur_substr[cur_substr.index(s[i]) + 1:]
            cur_substr.append(s[i])

        return max(max_length, len(cur_substr))
