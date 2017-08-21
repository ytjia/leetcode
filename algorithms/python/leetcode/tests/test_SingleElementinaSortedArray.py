# -*- coding: utf-8 -*-

# Authors: Y. Jia <ytjia.zju@gmail.com>

import unittest

from .. import SingleElementinaSortedArray


class test_SingleElementinaSortedArray(unittest.TestCase):
    solution = SingleElementinaSortedArray.Solution()

    def test_singleNonDuplicate(self):
        self.assertEqual(self.solution.singleNonDuplicate([1, 1, 2, 2, 3, 4, 4]), 3)
        self.assertEqual(self.solution.singleNonDuplicate([1, 1, 2, 3, 3, 4, 4, 8, 8]), 2)

        if __name__ == '__main__':
            unittest.main()
