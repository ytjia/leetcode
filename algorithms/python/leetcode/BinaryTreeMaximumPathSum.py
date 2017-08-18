# -*- coding: utf-8 -*-

# Authors: Y. Jia <ytjia.zju@gmail.com>

"""
Given a binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node
in the tree along the parent-child connections. The path must contain at least one node and does
not need to go through the root.

https://leetcode.com/problems/binary-tree-maximum-path-sum/description/
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        return self.partial_max_path_sum(root)[0]

    def partial_max_path_sum(self, root):
        """

        :param root:
        :return: max_path_sum, max_path_sum_end_with_root
        """
        if root.left and root.right:
            left_max_sum, left_max_sum_end_with_root = self.partial_max_path_sum(root.left)
            right_max_sum, right_max_sum_end_with_root = self.partial_max_path_sum(root.right)
            max_sum_end_with_root = max(root.val, root.val + left_max_sum_end_with_root,
                                        root.val + right_max_sum_end_with_root)
            max_sum = max(left_max_sum, right_max_sum, max_sum_end_with_root,
                          left_max_sum_end_with_root + root.val + right_max_sum_end_with_root)
        elif root.left:
            left_max_sum, left_max_sum_end_with_root = self.partial_max_path_sum(root.left)
            max_sum_end_with_root = max(root.val, left_max_sum_end_with_root + root.val)
            max_sum = max(left_max_sum, max_sum_end_with_root)
        elif root.right:
            right_max_sum, right_max_sum_end_with_root = self.partial_max_path_sum(root.right)
            max_sum_end_with_root = max(root.val, right_max_sum_end_with_root + root.val)
            max_sum = max(right_max_sum, max_sum_end_with_root)
        else:
            max_sum_end_with_root = root.val
            max_sum = root.val

        return max_sum, max_sum_end_with_root
