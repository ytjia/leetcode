# -*- coding: utf-8 -*-

# Authors: Y. Jia <ytjia.zju@gmail.com>

import unittest

from common.BinaryTree import BinaryTree
from .. import BinaryTreeMaximumPathSum


class test_BinaryTreeMaximumPathSum(unittest.TestCase):
    solution = BinaryTreeMaximumPathSum.Solution()

    def test_maxPathSum(self):
        self.assertEqual(self.solution.maxPathSum(BinaryTree.create_tree([1, 2, 3])[0]), 6)


if __name__ == '__main__':
    unittest.main()
