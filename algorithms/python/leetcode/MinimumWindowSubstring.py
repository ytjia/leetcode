# -*- coding: utf-8 -*-

# Authors: Y. Jia <ytjia.zju@gmail.com>

"""
Given a string S and a string T, find the minimum window in S which will contain all the
characters in T in complexity O(n).

https://leetcode.com/problems/minimum-window-substring/description/
"""


class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        mw = ""
        if not s or not t or len(s) == 0 or len(t) == 0:
            return mw
        t_char_cnt = len(t)
        t_char_dict = dict()
        for char in t:
            if char in t_char_dict:
                t_char_dict[char] += 1
            else:
                t_char_dict[char] = 1
        w_b = 0
        w_e = 0
        while w_e < len(s):
            if s[w_e] in t_char_dict:
                t_char_dict[s[w_e]] -= 1
                if t_char_dict[s[w_e]] >= 0:
                    t_char_cnt -= 1
            w_e += 1
            while t_char_cnt == 0:
                if len(mw) == 0 or w_e - w_b < len(mw):
                    mw = s[w_b:w_e]
                if s[w_b] in t_char_dict:
                    t_char_dict[s[w_b]] += 1
                    if t_char_dict[s[w_b]] > 0:
                        t_char_cnt += 1
                w_b += 1

        return mw
