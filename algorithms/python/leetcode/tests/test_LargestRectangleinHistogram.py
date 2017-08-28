# -*- coding: utf-8 -*-

# Authors: Y. Jia <ytjia.zju@gmail.com>

import unittest

from .. import LargestRectangleinHistogram


class TestLargestRectangleinHistogram(unittest.TestCase):
    solution = LargestRectangleinHistogram.Solution()

    def test_largestRectangleArea(self):
        self.assertEqual(self.solution.largestRectangleArea([2, 1, 5, 6, 2, 3]), 10)
        self.assertEqual(self.solution.largestRectangleArea([1]), 1)
        self.assertEqual(self.solution.largestRectangleArea([1, 1]), 2)
        self.assertEqual(self.solution.largestRectangleArea([2, 0, 2]), 2)


if __name__ == '__main__':
    unittest.main()
