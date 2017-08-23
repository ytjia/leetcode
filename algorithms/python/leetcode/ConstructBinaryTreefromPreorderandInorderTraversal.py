# -*- coding: utf-8 -*-

# Authors: Y. Jia <ytjia.zju@gmail.com>

"""
Given preorder and inorder traversal of a tree, construct the binary tree.

https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if len(preorder) == 0:
            return None

        root = TreeNode(preorder[0])
        ind = inorder.index(root.val)
        root.left = self.buildTree(preorder[1:ind + 1], inorder[0:ind])
        root.right = self.buildTree(preorder[ind + 1:], inorder[ind + 1:])

        return root
