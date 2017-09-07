# -*- coding: utf-8 -*-

# Authors: Y. Jia <ytjia.zju@gmail.com>


"""
Sort a linked list in O(n log n) time using constant space complexity.

https://leetcode.com/problems/sort-list/description/
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        p = head
        count = 1
        while p.next:
            count += 1
            p = p.next
        return self.merge_sort(head, count)

    def merge(self, h_a, h_b):
        p_a = h_a
        p_b = h_b
        pre_m = ListNode(0)
        p_m = pre_m
        while p_a and p_b:
            if p_a.val < p_b.val:
                p_m.next = p_a
                p_m = p_m.next
                p_a = p_a.next
            else:
                p_m.next = p_b
                p_m = p_m.next
                p_b = p_b.next
        if p_a:
            p_m.next = p_a
        else:
            p_m.next = p_b
        return pre_m.next

    def merge_sort(self, head, length):
        if head.next:
            mid = length / 2
            h_a = head
            t = head
            for i in range(mid - 1):
                t = t.next
            h_b = t.next
            t.next = None
            return self.merge(self.merge_sort(h_a, mid), self.merge_sort(h_b, length - mid))
        else:
            return head
