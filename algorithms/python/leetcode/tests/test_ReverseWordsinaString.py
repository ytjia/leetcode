# -*- coding: utf-8 -*-

# Authors: Y. Jia <ytjia.zju@gmail.com>

import unittest

from .. import ReverseWordsinaString


class test_ReverseWordsinaString(unittest.TestCase):
    solution = ReverseWordsinaString.Solution()

    def test_reverseWords(self):
        self.assertEqual(self.solution.reverseWords("hello world"), "world hello")
        self.assertEqual(self.solution.reverseWords("  "), "")
        self.assertEqual(self.solution.reverseWords(" a   b "), "b a")


if __name__ == '__main__':
    unittest.main()
