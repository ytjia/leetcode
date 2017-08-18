# -*- coding: utf-8 -*-

# Authors: Y. Jia <ytjia.zju@gmail.com>


"""
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left
to right, then right to left for the next level and alternate between).

https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        zigzag_list = list()
        if root is None:
            return zigzag_list
        node_list = list()
        node_level_list = list()
        node_list.append(root)
        node_level_list.append(1)
        node_zigzag_list = list()

        i = 0
        while i < len(node_list):
            cur_node = node_list[i]
            cur_node_level = node_level_list[i]
            if cur_node_level > len(node_zigzag_list):
                node_zigzag_list.append(list())
            node_zigzag_list[cur_node_level - 1].append(cur_node.val)
            if cur_node.left is not None:
                node_list.append(cur_node.left)
                node_level_list.append(cur_node_level + 1)
            if cur_node.right is not None:
                node_list.append(cur_node.right)
                node_level_list.append(cur_node_level + 1)
            i += 1

        for i in range(0, len(node_zigzag_list)):
            zigzag_list.append(list())
            if i % 2 == 0:
                for v in node_zigzag_list[i]:
                    zigzag_list[i].append(v)
            else:
                for v in node_zigzag_list[i][::-1]:
                    zigzag_list[i].append(v)

        return zigzag_list
