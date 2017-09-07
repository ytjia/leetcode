# -*- coding: utf-8 -*-

# Authors: Y. Jia <ytjia.zju@gmail.com>

import unittest

from .. import SortList


class test_SortList(unittest.TestCase):
    solution = SortList.Solution()

    n_a = SortList.ListNode(1)
    n_b = SortList.ListNode(2)
    n_c = SortList.ListNode(3)
    n_d = SortList.ListNode(4)
    n_d.next = n_a
    n_a.next = n_c
    n_c.next = n_b

    def test_sortList(self):
        self.assertEqual(self.solution.sortList(self.n_d), self.n_a)


if __name__ == '__main__':
    unittest.main()
