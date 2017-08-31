# -*- coding: utf-8 -*-

# Authors: Y. Jia <ytjia.zju@gmail.com>


"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

https://leetcode.com/problems/symmetric-tree/description/
"""

from Queue import Queue

from common.BinaryTree import TreeNode


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True

        def node_val(node):
            if node is None:
                return None
            else:
                return node.val

        left_bfs_value = map(node_val, self.btree_bfs(root.left))
        right_bfs_value = map(node_val, self.btree_bfs(root.right, False))

        return left_bfs_value == right_bfs_value

    def btree_bfs(self, root, left_first=True):
        node_list = list()
        if root is None:
            return node_list
        queue = Queue()
        queue.put(root)
        node_list.append(root)

        while not queue.empty():
            node = queue.get()
            if left_first:
                node_list.append(node.left)
                node_list.append(node.right)
                if node.left is not None:
                    queue.put(node.left)
                if node.right is not None:
                    queue.put(node.right)
            else:
                node_list.append(node.right)
                node_list.append(node.left)
                if node.right is not None:
                    queue.put(node.right)
                if node.left is not None:
                    queue.put(node.left)

        return node_list
