# -*- coding: utf-8 -*-

# Authors: Y. Jia <ytjia.zju@gmail.com>

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BinaryTree(object):
    @classmethod
    def create_tree(cls, node_v_list):
        if len(node_v_list) == 0:
            return None, list()
        node_list = list()
        node_list.append(TreeNode(node_v_list[0]))
        for i in range(1, len(node_v_list)):
            parent_node = node_list[(i - 1) / 2]
            is_left_node = (i - 1) % 2 == 0
            if node_v_list[i] == 'null':
                cur_node = None
            else:
                cur_node = TreeNode(node_v_list[i])
            if is_left_node:
                parent_node.left = cur_node
            else:
                parent_node.right = cur_node
            node_list.append(cur_node)

        return node_list[0], node_list
