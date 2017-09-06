# -*- coding: utf-8 -*-

# Authors: Y. Jia <ytjia.zju@gmail.com>

import unittest

from .. import MinimumWindowSubstring


class test_MinimumWindowSubstring(unittest.TestCase):
    solution = MinimumWindowSubstring.Solution()

    def test_minWindow(self):
        self.assertEqual(self.solution.minWindow("ADOBECODEBANC", "ABC"), "BANC")
        self.assertEqual(self.solution.minWindow("a", "a"), "a")


if __name__ == '__main__':
    unittest.main()
