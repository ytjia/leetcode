# -*- coding: utf-8 -*-

# Authors: Y. Jia <ytjia.zju@gmail.com




import unittest

from .. import GroupAnagrams


class test_GroupAnagrams(unittest.TestCase):
    solution = GroupAnagrams.Solution()

    def test_groupAnagrams(self):
        self.assertSequenceEqual(
                self.solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]),
                [
                    ["ate", "eat", "tea"],
                    ["nat", "tan"],
                    ["bat"]
                ])
        self.assertSequenceEqual(self.solution.groupAnagrams([]), [])
        self.assertSequenceEqual(self.solution.groupAnagrams(['a', 'b', 'ab', 'ba']),
                                 [['a'], ['b'], ['ab', 'ba']])

        if __name__ == '__main__':
            unittest.main()
