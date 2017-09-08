# -*- coding: utf-8 -*-

# Authors: Y. Jia <ytjia.zju@gmail.com>

"""
You are given two non-empty linked lists representing two non-negative integers. The digits are
stored in reverse order and each of their nodes contain a single digit. Add the two numbers and
return it as a linked list.

https://leetcode.com/problems/add-two-numbers/description/
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        pre_new_num = ListNode(-1)
        new_num = pre_new_num

        while l1 and l2:
            sum_l = l1.val + l2.val + carry
            carry = sum_l / 10
            new_digit = ListNode(sum_l % 10)
            new_num.next = new_digit
            new_num = new_num.next
            l1 = l1.next
            l2 = l2.next

        while l1:
            sum_l = l1.val + carry
            carry = sum_l / 10
            new_digit = ListNode(sum_l % 10)
            new_num.next = new_digit
            new_num = new_num.next
            l1 = l1.next

        while l2:
            sum_l = l2.val + carry
            carry = sum_l / 10
            new_digit = ListNode(sum_l % 10)
            new_num.next = new_digit
            new_num = new_num.next
            l2 = l2.next

        if carry > 0:
            new_digit = ListNode(carry)
            new_num.next = new_digit
        return pre_new_num.next
