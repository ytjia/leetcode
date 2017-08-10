#!/usr/bin python
# -*- coding: utf-8 -*-

"""
Given a binary tree
Populate each next pointer to point to its next right node.
If there is no next right node, the next pointer should be set to NULL.
Initially, all next pointers are set to NULL.
Note:
You may only use constant extra space.
You may assume that it is a perfect binary tree (ie, all leaves are at the
same level, and every parent has two children).
https://oj.leetcode.com/problems/populating-next-right-pointers-in-each-node/
"""

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        queue = list()
        if root is None:
            return
        else:
            queue.append(root)
        i = 0
        while i < len(queue):
            p = queue[0]
            if p.left is None:
                break
            else:
                queue.append(p.left)
            if p.right is None:
                break
            else:
                queue.append(p.right)
        bound = cnt = 1
        i = 0
        queue_len  = len(queue)
        while cnt < queue_len:
            if i < cnt - 1:
                queue[i].next = queue[i+1]
            else:
                queue[i].next = None
            i += 1
            # TODO


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
        print(Solution().preorderTraversal(t))
