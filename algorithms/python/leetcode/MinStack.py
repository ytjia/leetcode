# -*- coding: utf-8 -*-

# Authors: Y. Jia <ytjia.zju@gmail.com>

"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.

https://leetcode.com/problems/min-stack/description/
"""


class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = list()
        self.min_list = list()

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        if len(self.min_list) == 0:
            self.min_list.append(x)
        elif  x < self.min_list[-1]:
            self.min_list.append(x)
        else:
            self.min_list.append(self.min_list[-1])

    def pop(self):
        """
        :rtype: void
        """
        cur_top = self.stack.pop()
        del self.min_list[-1]

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_list[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
