# -*- coding: utf-8 -*-

# Authors: Y. Jia <ytjia.zju@gmail.com>


"""
Given a digit string, return all possible letter combinations that the number could represent.
A mapping of digit to letters (just like on the telephone buttons) is given below.

https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
"""


class Solution(object):
    num_letter_map = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz',
        '0': ' '
    }

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        length = len(digits)
        if length == 0:
            return []

        combinations = list()
        if length == 1:
            for char in self.num_letter_map[digits[0]]:
                combinations.append(char)

        for char in self.num_letter_map[digits[0]]:
            for e_chars in self.letterCombinations(digits[1:]):
                combinations.append(char + e_chars)

        return combinations
