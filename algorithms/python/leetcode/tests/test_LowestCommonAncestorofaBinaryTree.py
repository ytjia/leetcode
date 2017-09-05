# -*- coding: utf-8 -*-

# Authors: Y. Jia <ytjia.zju@gmail.com>



import unittest

from common.BinaryTree import BinaryTree
from .. import LowestCommonAncestorofaBinaryTree


class test_LowestCommonAncestorofaBinaryTree(unittest.TestCase):
    solution = LowestCommonAncestorofaBinaryTree.Solution()
    root_1, nodes_1 = BinaryTree.create_tree(
            [37, -34, -48, 'null', -100, -100, 48, 'null', 'null', 'null', 'null', -54, 'null',
             -71, -22, 'null', 'null', 'null', 8])
    root_2, nodes_2 = BinaryTree.create_tree([1, 2])

    def test_lowestCommonAncestor(self):
        self.assertEqual(
                self.solution.lowestCommonAncestor(self.root_1, self.nodes_1[1], self.nodes_1[2]),
                self.nodes_1[0])
        self.assertEqual(
                self.solution.lowestCommonAncestor(self.root_1, self.nodes_1[4], self.nodes_1[5]),
                self.nodes_1[2])
        self.assertEqual(
                self.solution.lowestCommonAncestor(self.root_2, self.nodes_2[0], self.nodes_2[1]),
                self.nodes_2[0])

    def test_dfs(self):
        self.assertListEqual(self.solution.dfs(self.root_1, self.nodes_1[1])[1],
                             [self.nodes_1[0], self.nodes_1[1]])


if __name__ == '__main__':
    unittest.main()
