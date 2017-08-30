# -*- coding: utf-8 -*-

# Authors: Y. Jia <ytjia.zju@gmail.com>

"""
Given two binary trees and imagine that when you put one of them to cover the other, some nodes
of the two trees are overlapped while the others are not.

You need to merge them into a new binary tree. The merge rule is that if two nodes overlap,
then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be
used as the node of new tree.

https://leetcode.com/problems/merge-two-binary-trees/description/
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        new_root = None
        if t1 is None and t2 is None:
            return new_root
        elif t1 is None:
            new_root = t2
        elif t2 is None:
            new_root = t1
        else:
            new_root = TreeNode(t1.val + t2.val)
            new_root.left = self.mergeTrees(t1.left, t2.left)
            new_root.right = self.mergeTrees(t1.right, t2.right)
        return new_root
