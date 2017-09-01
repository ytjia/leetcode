# -*- coding: utf-8 -*-

# Authors: Y. Jia <ytjia.zju@gmail.com>

import unittest

from .. import TheSkylineProblem


class test_TheSkylineProblem(unittest.TestCase):
    solution = TheSkylineProblem.Solution()

    def test_getSkyline(self):
        self.assertEqual(
                self.solution.getSkyline(
                        [[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]),
                [[2, 10], [3, 15], [7, 12], [12, 0], [15, 10], [20, 8], [24, 0]])
        self.assertEqual(self.solution.getSkyline([[2, 4, 7], [2, 4, 5], [2, 4, 6]]),
                         [[2, 7], [4, 0]])
        self.assertEqual(self.solution.getSkyline(
                [[2, 4, 70], [3, 8, 30], [6, 100, 41], [7, 15, 70], [10, 30, 102], [15, 25, 76],
                 [60, 80, 91], [70, 90, 72], [85, 120, 59]]),
                         [[2, 70], [4, 30], [6, 41], [7, 70], [10, 102], [30, 41], [60, 91],
                          [80, 72], [90, 59], [120, 0]])


if __name__ == '__main__':
    unittest.main()
