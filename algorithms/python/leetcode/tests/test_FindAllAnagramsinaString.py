# -*- coding: utf-8 -*-

# Authors: Y. Jia <ytjia.zju@gmail.com>

import unittest

from .. import FindAllAnagramsinaString


class test_FindAllAnagramsinaString(unittest.TestCase):
    solution = FindAllAnagramsinaString.Solution()

    def test_findAnagrams(self):
        self.assertEqual(self.solution.findAnagrams("cbaebabacd", "abc"), [0, 6])
        self.assertEqual(self.solution.findAnagrams("", "abc"), [])
        self.assertEqual(self.solution.findAnagrams("dfasdf", "abc"), [])
        self.assertEqual(self.solution.findAnagrams("abab", "ab"), [0, 1, 2])


if __name__ == '__main__':
    unittest.main()
