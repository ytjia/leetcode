# -*- coding: utf-8 -*-

# Authors: Y. Jia <ytjia.zju@gmail.com>



import unittest

from .. import WordSearch


class test_WordSearch(unittest.TestCase):
    solution = WordSearch.Solution()

    def test_exist(self):
        self.assertEqual(self.solution.exist(
                [
                    ['A', 'B', 'C', 'E'],
                    ['S', 'F', 'C', 'S'],
                    ['A', 'D', 'E', 'E']
                ], 'ABCCE'), True)
        self.assertEqual(self.solution.exist(
                [
                    ['A', 'B', 'C', 'E'],
                    ['S', 'F', 'C', 'S'],
                    ['A', 'D', 'E', 'E']
                ], 'SEE'), True)
        self.assertEqual(self.solution.exist(
                [
                    ['A', 'B', 'C', 'E'],
                    ['S', 'F', 'C', 'S'],
                    ['A', 'D', 'E', 'E']
                ], 'ABCB'), False)


if __name__ == '__main__':
    unittest.main()
