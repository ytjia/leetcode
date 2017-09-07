# -*- coding: utf-8 -*-

# Authors: Y. Jia <ytjia.zju@gmail.com>

import unittest

from .. import LongestConsecutiveSequence


class test_LongestConsecutiveSequence(unittest.TestCase):
    solution = LongestConsecutiveSequence.Solution()

    def test_longestConsecutive(self):
        self.assertEqual(self.solution.longestConsecutive([100, 4, 200, 1, 3, 2]), 4)
        self.assertEqual(self.solution.longestConsecutive([1, 2, 0, 1]), 3)
        self.assertEqual(self.solution.longestConsecutive(
                [-7, -1, 3, -9, -4, 7, -3, 2, 4, 9, 4, -9, 8, -7, 5, -1, -7]), 4)
        self.assertEqual(self.solution.longestConsecutive(
                [4, 2, 2, -4, 0, -2, 4, -3, -4, -4, -5, 1, 4, -9, 5, 0, 6, -8, -1, -3, 6, 5, -8, -1,
                 -5, -1, 2, -9, 1]), 8)

        if __name__ == '__main__':
            unittest.main()
