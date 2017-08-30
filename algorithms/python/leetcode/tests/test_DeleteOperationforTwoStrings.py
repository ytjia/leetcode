# -*- coding: utf-8 -*-

# Authors: Y. Jia <ytjia.zju@gmail.com>

import unittest

from .. import DeleteOperationforTwoStrings


class test_DeleteOperationforTwoStrings(unittest.TestCase):
    solution = DeleteOperationforTwoStrings.Solution()

    def test_minDistance(self):
        self.assertEqual(self.solution.minDistance('abe', 'bef'), 2)
        self.assertEqual(self.solution.minDistance('abe', ''), 3)


if __name__ == '__main__':
    unittest.main()
