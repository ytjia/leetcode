#!/usr/bin python
# -*- coding: utf-8 -*-

"""
Given a linked list, determine if it has a cycle in it.
Follow up:
Can you solve it without using extra space?
https://oj.leetcode.com/problems/linked-list-cycle/
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        if head == None:
            return False
        else:
            step1 = step2 = head
            while step1.next != None and step2.next != None \
                and step2.next.next != None:
                step1 = step1.next
                step2 = step2.next.next
                if step1.val == step2.val:
                    return True
                else:
                    pass
            return False

if __name__ == '__main__':
    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(3)
    l4 = ListNode(4)
    l1.next = l2
    l2.next = l3
    l3.next = l1
    test_case = [
        l1,
        l4
        ]
    for t in test_case:
        print(Solution().hasCycle(t))
