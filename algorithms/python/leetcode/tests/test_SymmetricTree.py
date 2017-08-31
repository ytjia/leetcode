# -*- coding: utf-8 -*-

# Authors: Y. Jia <ytjia.zju@gmail.com>

import unittest

from common.BinaryTree import BinaryTree
from .. import SymmetricTree


class test_SymmetricTree(unittest.TestCase):
    solution = SymmetricTree.Solution()

    root1 = BinaryTree.create_tree([1, 2, 2, 3, 4, 4, 3])[0]

    def test_isSymmetric(self):
        self.assertEqual(
                self.solution.isSymmetric(self.root1), True)
        self.assertEqual(
                self.solution.isSymmetric(
                        BinaryTree.create_tree([1, 2, 2, 'null', 3, 'null', 3])[0]),
                False)

    def test_btree_bfs(self):
        self.assertListEqual(map(lambda node: node.val, self.solution.btree_bfs(self.root1)),
                             [1, 2, 2, 3, 4, 4, 3])


if __name__ == '__main__':
    unittest.main()
