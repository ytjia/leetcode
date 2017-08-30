# -*- coding: utf-8 -*-

# Authors: Y. Jia <ytjia.zju@gmail.com>

"""
Given two words word1 and word2, find the minimum number of steps required to make word1 and
word2 the same, where in each step you can delete one character in either string.

https://leetcode.com/problems/delete-operation-for-two-strings/description/
"""


class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        lcs = self.longest_common_sequence(word1, word2)

        return len(word1) + len(word2) - 2 * lcs

    def longest_common_sequence(self, word1, word2):
        """

        :param word1:
        :param word2:
        :return:
        """
        length_w1 = len(word1)
        length_w2 = len(word2)
        dp = list()
        for i in range(length_w1 + 1):
            dp.append(list())
            for j in range(length_w2 + 1):
                dp[i].append(0)

        for i in range(1, length_w1 + 1):
            for j in range(1, length_w2 + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[length_w1][length_w2]
