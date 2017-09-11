# -*- coding: utf-8 -*-

# Authors: Y. Jia <ytjia.zju@gmail.com>


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return 'TreeNode({})'.format(self.val)


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

    @classmethod
    def deserialize(cls, string):
        if string == '{}':
            return None
        nodes = [None if val == 'null' else TreeNode(int(val))
                 for val in string.strip('[]{}').split(',')]
        kids = nodes[::-1]
        root = kids.pop()
        for node in nodes:
            if node:
                if kids:
                    node.left = kids.pop()
                if kids:
                    node.right = kids.pop()
        return root


def draw_tree(root):
    def height(node):
        return 1 + max(height(node.left), height(node.right)) if node else -1

    def jump_to(x, y):
        t.penup()
        t.goto(x, y)
        t.pendown()

    def draw(node, x, y, dx):
        if node:
            t.goto(x, y)
            jump_to(x, y - 20)
            t.write(node.val, align='center', font=('Arial', 12, 'normal'))
            draw(node.left, x - dx, y - 60, dx / 2)
            jump_to(x, y - 20)
            draw(node.right, x + dx, y - 60, dx / 2)

    import turtle
    t = turtle.Turtle()
    t.speed(0)
    turtle.delay(0)
    h = height(root)
    jump_to(0, 30 * h)
    draw(root, 0, 30 * h, 40 * h)
    t.hideturtle()
    turtle.mainloop()


if __name__ == '__main__':
    # draw_tree(BinaryTree.deserialize('[1,2,3,null,null,4,null,null,5]'))
    draw_tree(BinaryTree.deserialize(
            '[2,1,3,0,7,9,1,2,null,1,0,null,null,8,8,null,null,null,null,7]'))
