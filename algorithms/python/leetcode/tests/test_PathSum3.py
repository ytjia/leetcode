# -*- coding: utf-8 -*-

# Authors: Y. Jia <ytjia.zju@gmail.com>

import unittest

from common.BinaryTree import BinaryTree
from .. import PathSum3


class test_PathSum3(unittest.TestCase):
    solution = PathSum3.Solution()

    def test_pathSum(self):
        root = BinaryTree.create_tree([10, 5, -3, 3, 2, 'null', 11, 3, -2, 'null', 1])[0]
        self.assertEqual(self.solution.pathSum(root, 8), 3)


if __name__ == '__main__':
    unittest.main()
