# -*- coding: utf-8 -*-

# Authors: Y. Jia <ytjia.zju@gmail.com>

import unittest

from .. import SumofSquareNumbers


class test_SumofSquareNumbers(unittest.TestCase):
    solution = SumofSquareNumbers.Solution()

    def test_sqrt_binary_search(self):
        self.assertTrue(self.solution.sqrt_binary_search(9, 1, 6))
        self.assertTrue(self.solution.sqrt_binary_search(16, 1, 6))
        self.assertFalse(self.solution.sqrt_binary_search(49, 1, 6))
        self.assertFalse(self.solution.sqrt_binary_search(15, 1, 6))

    def test_isSquareNum(self):
        self.assertEqual(self.solution.isSquareNum(0), (True, 0))
        self.assertEqual(self.solution.isSquareNum(1), (True, 1))
        self.assertEqual(self.solution.isSquareNum(2), (False, None))
        self.assertEqual(self.solution.isSquareNum(3), (False, None))
        self.assertEqual(self.solution.isSquareNum(4), (True, 2))
        self.assertEqual(self.solution.isSquareNum(15), (False, None))
        self.assertEqual(self.solution.isSquareNum(100), (True, 10))
        self.assertEqual(self.solution.isSquareNum(9999), (False, None))

    def test_judgeSquareSum(self):
        self.assertTrue(self.solution.judgeSquareSum(0))
        self.assertTrue(self.solution.judgeSquareSum(1))
        self.assertTrue(self.solution.judgeSquareSum(2))
        self.assertTrue(self.solution.judgeSquareSum(16))
        self.assertTrue(self.solution.judgeSquareSum(225))
        self.assertFalse(self.solution.judgeSquareSum(3))
        self.assertFalse(self.solution.judgeSquareSum(6))


if __name__ == '__main__':
    unittest.main()
