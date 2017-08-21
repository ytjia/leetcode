# -*- coding: utf-8 -*-

# Authors: Y. Jia <ytjia.zju@gmail.com>

import unittest

from ..MergeIntervals import Solution, Interval


class test_MergeIntervals(unittest.TestCase):
    solution = Solution()

    def test_merge(self):
        self.assertEqual(self.solution.merge(
                [Interval(1, 3), Interval(2, 6), Interval(8, 10), Interval(15, 18)]),
                         [Interval(1, 6), Interval(8, 10), Interval(15, 18)])


if __name__ == '__main__':
    unittest.main()
