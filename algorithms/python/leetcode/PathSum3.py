# -*- coding: utf-8 -*-

# Authors: Y. Jia <ytjia.zju@gmail.com>

"""
You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling
only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

https://leetcode.com/problems/path-sum-iii/description/
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if root is None:
            return 0

        return self.path_sum_partial(root, sum)

    def path_sum_partial(self, root, sum, parent_in_path=False):
        roots_sum = 0
        if root.val == sum:
            roots_sum += 1
        if root.left is not None:
            roots_sum += self.path_sum_partial(root.left, sum - root.val, True)
            if not parent_in_path:
                roots_sum += self.path_sum_partial(root.left, sum, False)
        if root.right is not None:
            roots_sum += self.path_sum_partial(root.right, sum - root.val, True)
            if not parent_in_path:
                roots_sum += self.path_sum_partial(root.right, sum, False)
        return roots_sum
