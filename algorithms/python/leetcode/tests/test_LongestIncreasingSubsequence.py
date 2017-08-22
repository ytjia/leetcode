# -*- coding: utf-8 -*-

# Authors: Y. Jia <ytjia.zju@gmail.com>

import unittest

from .. import LongestIncreasingSubsequence


class test_LongestIncreasingSubsequence(unittest.TestCase):
    solution = LongestIncreasingSubsequence.Solution()

    def test_lengthOfLIS(self):
        self.assertEqual(self.solution.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]), 4)
        self.assertEqual(self.solution.lengthOfLIS([2, 2]), 1)
        self.assertEqual(self.solution.lengthOfLIS([3, 5, 6, 2, 5, 4, 19, 5, 6, 7, 12]), 6)

    def test_binary_search_just_less(self):
        self.assertEqual(self.solution.binary_search_just_less([2, 3, 4, 5, 6], 5), 2)
        self.assertEqual(self.solution.binary_search_just_less([2, 3, 4, 7, 9, 10], 8), 3)
        self.assertEqual(self.solution.binary_search_just_less([2, 3, 4, 7, 9, 10], 1), -1)
        self.assertEqual(self.solution.binary_search_just_less([2, 3, 4, 7, 9, 10], 15), 5)
        self.assertEqual(self.solution.binary_search_just_less([], 15), -1)
        self.assertEqual(self.solution.binary_search_just_less([2, 4, 6, 9], 5), 1)


if __name__ == '__main__':
    unittest.main()
