# -*- coding: utf-8 -*-

# Authors: Y. Jia <ytjia.zju@gmail.com>

import unittest


from .. import LongestValidParentheses

class test_LongestValidParentheses(unittest.TestCase):
    solution = LongestValidParentheses.Solution()

    def test_longestValidParentheses(self):
        self.assertEqual(self.solution.longestValidParentheses(')()())'), 4)
        self.assertEqual(self.solution.longestValidParentheses(')()'), 2)
        self.assertEqual(self.solution.longestValidParentheses(')'), 0)
        self.assertEqual(self.solution.longestValidParentheses('(((((((()))))))'), 14)
        self.assertEqual(self.solution.longestValidParentheses('()(())'), 6)


if __name__ == '__main__':
    unittest.main()
