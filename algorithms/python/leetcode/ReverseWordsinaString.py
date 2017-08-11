# -*- coding: utf-8 -*-

# Authors: Y. Jia <ytjia.zju@gmail.com>

"""
Given an input string, reverse the string word by word.

For example,
Given s = "the sky is blue",
return "blue is sky the".

https://leetcode.com/problems/reverse-words-in-a-string/description/
"""


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        word_list = s.strip().split(" ")
        word_list = filter(lambda _: len(_) > 0, word_list)
        word_list.reverse()

        return " ".join(word_list)
