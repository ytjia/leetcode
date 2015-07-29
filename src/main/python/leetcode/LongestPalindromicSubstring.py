#!/usr/bin python       
# -*- coding: utf-8 -*-

"""
Given a string S, find the longest palindromic substring in S. 
You may assume that the maximum length of S is 1000, and there 
exists one unique longest palindromic substring.
https://oj.leetcode.com/problems/longest-palindromic-substring/
"""

class Solution:
    # @return a string
    def longestPalindrome(self, s):
        # TODO algorithm optimation, test case time out
        max_length = 0
        longest_subs = ''
        s_length = len(s)
        i = 0
        while i < s_length:
            length_a, subs_a = self.centerMe(s, s_length, i)
            length_b, subs_b = self.laterMe(s, s_length, i)
            if length_a > length_b:
                cur_len = length_a
                cur_subs = subs_a
            else:
                cur_len = length_b
                cur_subs = subs_b
            if cur_len > max_length:
                max_length = cur_len
                longest_subs = cur_subs
            else:
                pass
            i += 1
        return longest_subs

    @classmethod
    def centerMe(self, s, s_length, i):
        radias = 0
        j = 1
        while (i - j >= 0) and (i + j < s_length) and (s[i-j] == s[i+j]):
            radias += 1
            j += 1
        return radias*2+1, s[i-radias : i+radias+1]

    @classmethod
    def laterMe(self, s, s_length, i):
        radias = 0
        j = 0
        while (i - j - 1 >= 0) and (i + j < s_length) and (s[i-j-1] == s[i+j]):
            radias += 1
            j += 1
        return radias*2, s[i-radias : i+radias]

if __name__ == '__main__':
    test_case = [
        'hello',
        'asdfaasddsa',
        'difhhfertyuytre'
        ]
    for test_s in test_case:
        subs = Solution().longestPalindrome(test_s)
        print subs