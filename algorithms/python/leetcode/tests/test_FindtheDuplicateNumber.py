# -*- coding: utf-8 -*-

# Authors: Y. Jia <ytjia.zju@gmail.com>

import unittest

from .. import FindtheDuplicateNumber


class test_FindtheDuplicateNumber(unittest.TestCase):
    solution = FindtheDuplicateNumber.Solution()

    def test_findDuplicate(self):
        self.assertEqual(self.solution.findDuplicate([5, 3, 1, 2, 4, 2]), 2)


if __name__ == '__main__':
    unittest.main()
