#!/usr/bin python       
# -*- coding: utf-8 -*-

"""
Given a binary tree, return the preorder traversal of its nodes' values.
https://oj.leetcode.com/problems/binary-tree-preorder-traversal/
"""

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def preorderTraversal(self, root):
        result = []
        if root == None:
            return result
        else:
            result.append(root.val)
            result += self.preorderTraversal(root.left)
            result += self.preorderTraversal(root.right)
            return result
 
if __name__ == '__main__':
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n1.left = n2
    n2.right = n3
    n3.right = n4
    test_case = [
        n3,
        n1,
        n4
        ]
    for t in test_case:
        print Solution().preorderTraversal(t)