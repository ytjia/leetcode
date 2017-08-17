# -*- coding: utf-8 -*-

# Authors: Y. Jia <ytjia.zju@gmail.com>

import unittest

from .. import Permutations


class test_Permutations(unittest.TestCase):
    solution = Permutations.Solution()

    def test_permute(self):
        self.assertEqual(self.solution.permute([]), [])
        self.assertEqual(self.solution.permute([1]), [[1]])
        self.assertEqual(self.solution.permute([1, 2]), [[1, 2], [2, 1]])
        self.assertEqual(self.solution.permute([1, 2, 3]),
                         [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]])


if __name__ == '__main__':
    unittest.main()
