# -*- coding: utf-8 -*-

# Authors: Y. Jia <ytjia.zju@gmail.com>

import unittest

from .. import TrappingRainWater


class test_TrappingRainWater(unittest.TestCase):
    solution = TrappingRainWater.Solution()

    def test_trap(self):
        self.assertEqual(self.solution.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]), 6)
        self.assertEqual(self.solution.trap([]), 0)
        self.assertEqual(self.solution.trap([0, 0]), 0)
        self.assertEqual(self.solution.trap([0, 1]), 0)
        self.assertEqual(self.solution.trap([4, 2, 3]), 1)

        if __name__ == '__main__':
            unittest.main()
