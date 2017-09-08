# -*- coding: utf-8 -*-

# Authors: Y. Jia <ytjia.zju@gmail.com>

import unittest

from .. import MinimumHeightTrees


class test_MinimumHeightTrees(unittest.TestCase):
    solution = MinimumHeightTrees.Solution()

    def test_findMinHeightTrees(self):
        self.assertEqual(self.solution.findMinHeightTrees(4, [[1, 0], [1, 2], [1, 3]]), [1])


if __name__ == '__main__':
    unittest.main()
