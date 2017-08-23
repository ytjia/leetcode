# -*- coding: utf-8 -*-

# Authors: Y. Jia <ytjia.zju@gmail.com>

import unittest

from .. import TaskScheduler


class test_TaskScheduler(unittest.TestCase):
    solution = TaskScheduler.Solution()

    def test_leastInterval(self):
        self.assertEqual(self.solution.leastInterval(['A', 'A', 'B', 'B'], 3), 6)
        self.assertEqual(self.solution.leastInterval(['A', 'A', 'A', 'B', 'B', 'B'], 2), 8)


if __name__ == '__main__':
    unittest.main()
