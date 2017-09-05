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
        node_list = list()
        if len(node_v_list) == 0:
            return None, node_list
        node_list.append(TreeNode(node_v_list[0]))
        i = 0
        j = 1
        is_left = True
        while i < len(node_list) and j < len(node_v_list):
            if node_v_list[j] == 'null':
                cur_node = None
            else:
                cur_node = TreeNode(node_v_list[j])
                node_list.append(cur_node)
            if is_left:
                node_list[i].left = cur_node
            else:
                node_list[i].right = cur_node
                i += 1
            is_left = not is_left
            j += 1

        return node_list[0], node_list
