# -*- coding: utf-8 -*-

# Authors: Y. Jia <ytjia.zju@gmail.com>

"""
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will
not be larger than 20,100.

The order of output does not matter.

https://leetcode.com/problems/find-all-anagrams-in-a-string/description/
"""


class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        lens_s = len(s)
        lens_p = len(p)
        indices_list = list()
        if lens_s == 0 or lens_s < lens_p:
            return indices_list
        p_char_stat = list()
        s_s_char_stat = list()
        for i in range(26):
            p_char_stat.append(0)
            s_s_char_stat.append(0)

        for char in p:
            p_char_stat[ord(char) - ord('a')] += 1

        for i in range(lens_p - 1):
            s_s_char_stat[ord(s[i]) - ord('a')] += 1

        for i in range(lens_p - 1, lens_s):
            judged_start = i - lens_p + 1
            s_s_char_stat[ord(s[i]) - ord('a')] += 1
            if s_s_char_stat == p_char_stat:
                indices_list.append(judged_start)
            s_s_char_stat[ord(s[judged_start]) - ord('a')] -= 1

        return indices_list
