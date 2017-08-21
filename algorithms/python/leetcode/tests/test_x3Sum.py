# -*- coding: utf-8 -*-

# Authors: Y. Jia <ytjia.zju@gmail.com>

import unittest

from common import sort_util
from .. import x3Sum


class test_x3Sum(unittest.TestCase):
    solution = x3Sum.Solution()

    def test_threeSum(self):
        self.assertEqual(self.solution.threeSum([-1, -1, 0, 2, 1]),
                         [[-1, 2, -1], [-1, 1, 0]])

    def test_binary_search(self):
        self.assertTrue(sort_util.binary_search([1, 2, 3], 2))
        self.assertTrue(sort_util.binary_search([1, 2, 3], 3))
        self.assertFalse(sort_util.binary_search([1, 2, 3], 4))
        self.assertFalse(sort_util.binary_search([], 4))
        self.assertFalse(sort_util.binary_search([1], 4))


if __name__ == '__main__':
    unittest.main()
