# -*- coding: utf-8 -*-

# Authors: Y. Jia <ytjia.zju@gmail.com>

"""
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

https://leetcode.com/problems/merge-k-sorted-lists/description/
"""

from Queue import PriorityQueue


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        header = ListNode(None)

        p_queue = PriorityQueue()
        for node in lists:
            if node:
                p_queue.put((node.val, node))

        cur = header
        while not p_queue.empty():
            t_node = p_queue.get()[1]
            if t_node.next is not None:
                p_queue.put((t_node.next.val, t_node.next))
            cur.next = t_node
            cur = cur.next

        return header.next
