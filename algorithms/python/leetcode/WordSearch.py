# -*- coding: utf-8 -*-

# Authors: Y. Jia <ytjia.zju@gmail.com>

"""
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells
are those horizontally or vertically neighboring. The same letter cell may not be used more than
once.

https://leetcode.com/problems/word-search/description/
"""


class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board:
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, i, j, word):
                    return True
        return False

    def dfs(self, board, i, j, word):
        """
        Depth-First-Search
        :param board:
        :param i:
        :param j:
        :param word:
        :return:
        """
        if len(word) == 0:
            return True
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[0]:
            return False
        tmp = board[i][j]
        board[i][j] = '#'
        status = self.dfs(board, i - 1, j, word[1:]) or self.dfs(board, i + 1, j, word[1:]) \
                 or self.dfs(board, i, j - 1, word[1:]) or self.dfs(board, i, j + 1, word[1:])
        board[i][j] = tmp
        return status
