# -*- coding: utf-8 -*-

# Authors: Y. Jia <ytjia.zju@gmail.com>


import unittest

from common.BinaryTree import BinaryTree
from .. import BinaryTreeZigzagLevelOrderTraversal


class test_BinaryTreeZigzagLevelOrderTraversal(unittest.TestCase):
    solution = BinaryTreeZigzagLevelOrderTraversal.Solution()

    def test_zigzagLevelOrder(self):
        A = BinaryTreeZigzagLevelOrderTraversal.TreeNode(3)
        B = BinaryTreeZigzagLevelOrderTraversal.TreeNode(9)
        C = BinaryTreeZigzagLevelOrderTraversal.TreeNode(20)
        D = BinaryTreeZigzagLevelOrderTraversal.TreeNode(15)
        E = BinaryTreeZigzagLevelOrderTraversal.TreeNode(7)
        A.left = B
        A.right = C
        C.left = D
        C.right = E

        self.assertEqual(self.solution.zigzagLevelOrder(A), [[3], [20, 9], [15, 7]])
        self.assertEqual(self.solution.zigzagLevelOrder(None), [])

        root = BinaryTree.create_tree([1, 2, 3, 4, 'null', 'null', 5])[0]
        self.assertEqual(self.solution.zigzagLevelOrder(root), [[1], [3, 2], [4, 5]])


if __name__ == '__main__':
    unittest.main()
