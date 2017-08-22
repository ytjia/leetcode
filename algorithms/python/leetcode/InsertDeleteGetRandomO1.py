# -*- coding: utf-8 -*-

# Authors: Y. Jia <ytjia.zju@gmail.com>

"""
Design a data structure that supports all following operations in average O(1) time.

1. insert(val): Inserts an item val to the set if not already present.
2. remove(val): Removes an item val from the set if present.
3. getRandom: Returns a random element from current set of elements. Each element must have the same
probability of being returned.

https://leetcode.com/problems/insert-delete-getrandom-o1/description/
"""

import random


class RandomizedSet(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = []
        self.pos = dict()

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified
        element.
        :type val: int
        :rtype: bool
        """
        if val in self.pos:
            return False
        else:
            self.nums.append(val)
            self.pos[val] = len(self.nums) - 1
            return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.pos:
            last, idx = self.nums[-1], self.pos[val]
            self.pos[last], self.nums[idx] = idx, last
            self.nums.pop()
            self.pos.pop(val)
            return True
        else:
            return False

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return self.nums[random.randint(0, len(self.nums) - 1)]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
