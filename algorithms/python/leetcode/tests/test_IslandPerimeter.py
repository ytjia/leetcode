# -*- coding: utf-8 -*-

# Authors: Y. Jia <ytjia.zju@gmail.com>



import unittest

from .. import IslandPerimeter


class test_IslandPerimeter(unittest.TestCase):
    solution = IslandPerimeter.Solution()

    def test_islandPerimeter(self):
        self.assertEqual(self.solution.islandPerimeter(
                [[0, 1, 0, 0],
                 [1, 1, 1, 0],
                 [0, 1, 0, 0],
                 [1, 1, 0, 0]]), 16)


if __name__ == '__main__':
    unittest.main()
