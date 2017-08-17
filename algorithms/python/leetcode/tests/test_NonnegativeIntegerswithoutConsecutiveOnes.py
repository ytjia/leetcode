# -*- coding: utf-8 -*-

# Authors: Y. Jia <ytjia.zju@gmail.com>

import unittest

from .. import NonnegativeIntegerswithoutConsecutiveOnes

class TestNonnegativeIntegerswithoutConsecutiveOnes(unittest.TestCase):
    solution = NonnegativeIntegerswithoutConsecutiveOnes.Solution()

    def test_findIntegers(self):
        self.assertEqual(self.solution.findIntegers(1), 2)
        self.assertEqual(self.solution.findIntegers(3), 3)
        self.assertEqual(self.solution.findIntegers(5), 5)
        self.assertEqual(self.solution.findIntegers(8), 6)

    def test_find_binary_bit_pos(self):
        self.assertEqual(self.solution.find_binary_bit_pos(0), list())
        self.assertEqual(self.solution.find_binary_bit_pos(1), [0])
        self.assertEqual(self.solution.find_binary_bit_pos(5), [0, 2])
        self.assertEqual(self.solution.find_binary_bit_pos(8), [3])
        self.assertEqual(self.solution.find_binary_bit_pos(15), [0, 1, 2, 3])

    def test_stat_bit_cnt(self):
        self.assertEqual(self.solution.stat_bit_cnt(0), [2])
        self.assertEqual(self.solution.stat_bit_cnt(1), [2, 1])
        self.assertEqual(self.solution.stat_bit_cnt(2), [2, 1, 2])
        self.assertEqual(self.solution.stat_bit_cnt(3), [2, 1, 2, 3])


if __name__ == '__main__':
    unittest.main()
