# -*- coding: utf-8 -*-

# Authors: Y. Jia <ytjia.zju@gmail.com>

import unittest

from .. import UniquePaths


class test_UniquePaths(unittest.TestCase):
    solution = UniquePaths.Solution()

    def test_uniquePaths(self):
        self.assertEqual(self.solution.uniquePaths(2, 2), 2)
        self.assertEqual(self.solution.uniquePaths(3, 2), 3)


if __name__ == '__main__':
    unittest.main()
