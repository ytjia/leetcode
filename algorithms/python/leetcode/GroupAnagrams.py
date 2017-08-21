# -*- coding: utf-8 -*-

# Authors: Y. Jia <ytjia.zju@gmail.com>

"""
Given an array of strings, group anagrams together.

https://leetcode.com/problems/group-anagrams/description/
"""


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        grouped_anagrams = list()
        lens = len(strs)
        if lens == 0:
            return grouped_anagrams

        anagrams_dict = dict()
        for s in strs:
            char_dict = {}
            for char in s:
                if char in char_dict:
                    char_dict[char] += 1
                else:
                    char_dict[char] = 1
            char_set = frozenset(char_dict.items())
            if char_set in anagrams_dict:
                anagrams_dict[char_set].append(s)
            else:
                anagrams_dict[char_set] = [s]

        for k, v in anagrams_dict.items():
            grouped_anagrams.append(v)

        return grouped_anagrams
