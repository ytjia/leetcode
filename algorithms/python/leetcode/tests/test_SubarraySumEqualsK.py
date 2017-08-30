# -*- coding: utf-8 -*-

# Authors: Y. Jia <ytjia.zju@gmail.com>

import unittest

from .. import SubarraySumEqualsK


class test_SubarraySumEqualsK(unittest.TestCase):
    solution = SubarraySumEqualsK.Solution()

    def test_subarraySum(self):
        self.assertEqual(self.solution.subarraySum([1, 2, 3], 3), 2)
        self.assertEqual(self.solution.subarraySum([1], 0), 0)


if __name__ == '__main__':
    unittest.main()
