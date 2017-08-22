# -*- coding: utf-8 -*-

# Authors: Y. Jia <ytjia.zju@gmail.com>

"""
Reverse a singly linked list.

https://leetcode.com/problems/reverse-linked-list/description/
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        node = head
        while node:
            tmp = node.next
            node.next = prev
            prev = node
            node = tmp

        return prev
