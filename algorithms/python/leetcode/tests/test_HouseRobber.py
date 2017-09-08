# -*- coding: utf-8 -*-

# Authors: Y. Jia <ytjia.zju@gmail.com>



import unittest

from .. import HouseRobber


class test_HouseRobber(unittest.TestCase):
    solution = HouseRobber.Solution()

    def test_rob(self):
        self.assertEqual(self.solution.rob([0, 0, 0]), 0)

        if __name__ == '__main__':
            unittest.main()
