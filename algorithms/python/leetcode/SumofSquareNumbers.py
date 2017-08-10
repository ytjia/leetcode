# -*- coding: utf-8 -*-

# Authors: Y. Jia <ytjia.zju@gmail.com>

"""
Given a non-negative integer c, your task is to decide whether there're two integers a and b such
that a2 + b2 = c.

https://leetcode.com/problems/sum-of-square-numbers/description/
"""


class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        i = 0
        si = i * i
        while si <= c:
            b = c - si
            if (int(b ** 0.5)) ** 2 == b:
                return True
            i += 1
            si = i * i

        return False

    # ------ code below are not used to solve this problem ------

    @classmethod
    def sqrt_binary_search(cls, t, start, end):
        """
        judge if there is x between start and end that x * x == t
        :param t: target integer
        :return: True or False
        """
        if start > end:
            return False

        middle = start + (end - start) / 2
        if t == middle * middle:
            return True
        elif t < middle * middle:
            return Solution.sqrt_binary_search(t, start, middle - 1)
        else:
            return Solution.sqrt_binary_search(t, middle + 1, end)

    @classmethod
    def isSquareNum(cls, x):
        """
        judge if x is some integer's square.
        :param x:
        :return: (True, the integer) or (False, None)
        """
        assert x >= 0

        if x == 0 or x == 1:
            return True, x

        dx = x
        while dx / 2 > 0:
            if dx % 2 > 0:
                z = dx / 2 + 1
            else:
                z = dx / 2
            if z * z == x:
                return True, z
            elif z * z < x:
                break
            else:
                dx = z

        for i in range(z, z * 2):
            if i * i == x:
                return True, i

        return False, None
