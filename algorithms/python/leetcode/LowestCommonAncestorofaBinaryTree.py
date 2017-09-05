# -*- coding: utf-8 -*-

# Authors: Y. Jia <ytjia.zju@gmail.com>


"""
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        p_path = self.dfs(root, p)[1]
        q_path = self.dfs(root, q)[1]
        lca = None
        i = 0
        while i < len(p_path) and i < len(q_path):
            if p_path[i] != q_path[i]:
                break
            else:
                lca = p_path[i]
                i += 1
        return lca

    def dfs(self, root, target):
        if root is None:
            return False, None
        if root == target:
            return True, [root]
        if root.left:
            found, path = self.dfs(root.left, target)
            if found:
                return True, [root] + path
        if root.right:
            found, path = self.dfs(root.right, target)
            if found:
                return True, [root] + path
        return False, None
