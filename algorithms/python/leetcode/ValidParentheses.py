# -*- coding: utf-8 -*-

# Authors: Y. Jia <ytjia.zju@gmail.com>

"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the
input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]"
are not.

https://leetcode.com/problems/valid-parentheses/description/
"""


class Solution(object):
    _p_left_set = set('({[')
    _p_dict = {')': '(', '(': ')', '{': '}', '}': '{', '[': ']', ']': '['}

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = list()
        for c in s:
            if c in self._p_left_set:
                stack.append(c)
            elif len(stack) > 0 and self._p_dict[c] == stack[-1]:
                stack.pop()
            else:
                return False
        if len(stack) == 0:
            return True
        else:
            return False
