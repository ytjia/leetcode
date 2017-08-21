# -*- coding: utf-8 -*-

# Authors: Y. Jia <ytjia.zju@gmail.com>

import unittest


from .. import SearchinRotatedSortedArray

class test_SearchinRotatedSortedArray(unittest.TestCase):
    solution = SearchinRotatedSortedArray.Solution()

    def test_search(self):
        self.assertEqual(self.solution.search([4, 5, 6, 0, 1, 2, 3,], 5), 1)
        self.assertEqual(self.solution.search([4, 5, 6, 0, 1, 2, 3,], 0), 3)
        self.assertEqual(self.solution.search([4, 5, 6, 0, 1, 2, 3,], 3), 6)
        self.assertEqual(self.solution.search([4, 5, 6, 0, 1, 2, 3,], 7), -1)
        self.assertEqual(self.solution.search([], 7), -1)


if __name__ == '__main__':
    unittest.main()
