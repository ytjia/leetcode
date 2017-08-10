#!/usr/bin python
# -*- coding: utf-8 -*-

"""
Given a binary tree, find its maximum depth.
The maximum depth is the number of nodes along the longest path
from the root node down to the farthest leaf node.
https://oj.leetcode.com/problems/maximum-depth-of-binary-tree/
"""

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def maxDepth(self, root):
        if root == None:
            cur_depth = 0
        elif root.left == None and root.right == None:
            cur_depth = 1
        elif root.left == None:
            cur_depth = 1 + self.maxDepth(root.right)
        elif root.right == None:
            cur_depth = 1 + self.maxDepth(root.left)
        else:
            cur_depth = 1 + max(self.maxDepth(root.right), self.maxDepth(root.left))
        return cur_depth

if __name__ == '__main__':
    r1 = TreeNode(1)
    r2 = TreeNode(2)
    r3 = TreeNode(3)
    r1.left = r2
    r2.right = r3
    test_case = [
        r1,
        r2,
        r3
        ]
    for test_s in test_case:
        subs = Solution().maxDepth(test_s)
        print(subs)
