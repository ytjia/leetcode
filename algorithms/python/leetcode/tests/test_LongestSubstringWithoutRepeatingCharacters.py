# -*- coding: utf-8 -*-

# Authors: Y. Jia <ytjia.zju@gmail.com>

import unittest

from .. import LongestSubstringWithoutRepeatingCharacters


class test_LongestSubstringWithoutRepeatingCharacters(unittest.TestCase):
    solution = LongestSubstringWithoutRepeatingCharacters.Solution()

    def test_lengthOfLongestSubstring(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring('pweekbdb'), 4)
        self.assertEqual(self.solution.lengthOfLongestSubstring('abcabcbb'), 3)
        self.assertEqual(self.solution.lengthOfLongestSubstring('bbbbb'), 1)
        self.assertEqual(self.solution.lengthOfLongestSubstring(''), 0)


if __name__ == '__main__':
    unittest.main()
