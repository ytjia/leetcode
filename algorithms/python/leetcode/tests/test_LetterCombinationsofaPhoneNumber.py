# -*- coding: utf-8 -*-

# Authors: Y. Jia <ytjia.zju@gmail.com>

import unittest

from .. import LetterCombinationsOfaPhoneNumber


class test_LetterCombinationsOfaPhoneNumber(unittest.TestCase):
    solution = LetterCombinationsOfaPhoneNumber.Solution()

    def test_letterCombinations(self):
        self.assertEqual(self.solution.letterCombinations('2'), ['a', 'b', 'c'])
        self.assertEqual(self.solution.letterCombinations('23'),
                         ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf'])


if __name__ == '__main__':
    unittest.main()
