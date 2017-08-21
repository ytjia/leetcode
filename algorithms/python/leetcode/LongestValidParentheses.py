# -*- coding: utf-8 -*-

# Authors: Y. Jia <ytjia.zju@gmail.com>


"""
Given a string containing just the characters '(' and ')', find the length of the longest valid (
well-formed) parentheses substring.

https://leetcode.com/problems/longest-valid-parentheses/description/
"""


class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        lens = len(s)
        if lens <= 1:
            return 0
        longest_pairs = 0
        end_with_pairs = list()
        stack = list()

        for i in range(lens):
            end_with_cur_pairs = 0
            if s[i] == '(':
                stack.append(i)
            else:
                if len(stack) > 0:
                    last_unpaired_left_index = stack.pop()
                    if last_unpaired_left_index - 1 >= 0:
                        end_with_cur_pairs = end_with_pairs[last_unpaired_left_index - 1] + \
                                             end_with_pairs[i - 1] + 1
                    else:
                        end_with_cur_pairs = end_with_pairs[i - 1] + 1
                else:
                    end_with_cur_pairs = 0
            end_with_pairs.append(end_with_cur_pairs)
            longest_pairs = max(longest_pairs, end_with_cur_pairs)

        return longest_pairs * 2
