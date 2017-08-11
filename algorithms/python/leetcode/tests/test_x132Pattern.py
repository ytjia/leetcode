# -*- coding: utf-8 -*-

# Authors: Y. Jia <ytjia.zju@gmail.com>

import unittest

from .. import x132Pattern


class test_x132Pattern(unittest.TestCase):
    solution = x132Pattern.Solution()

    def test_find132Pattern(self):
        self.assertFalse(self.solution.find132pattern([1, 2, 3, 4]))
        self.assertTrue(self.solution.find132pattern([3, 1, 4, 2]))
        self.assertTrue(self.solution.find132pattern([-1, 3, 2, 0]))
        self.assertTrue(self.solution.find132pattern([-2, 1, 2, -2, 1, 2]))


if __name__ == '__main__':
    unittest.main()
