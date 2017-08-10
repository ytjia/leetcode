# -*- coding: utf-8 -*-

# Authors: Y. Jia <ytjia.zju@gmail.com>

import unittest

from .. import MinStack


class test_MinStack(unittest.TestCase):
    def test_MinStack(self):
        stack = MinStack.MinStack()
        self.assertEqual(stack.push(-3), None)


if __name__ == '__main__':
    unittest.main()
