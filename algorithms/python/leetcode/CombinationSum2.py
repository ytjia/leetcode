#!/usr/bin python
# -*- coding: utf-8 -*-

"""
Given a collection of candidate numbers (C) and a target number (T),
find all unique combinations in C where the candidate numbers sums to T.
Each number in C may only be used once in the combination.
http://oj.leetcode.com/problems/combination-sum-ii/
"""

class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum2(self, candidates, target):
        candi_unique = set(candidates)
        candi_sorted = tuple(sorted(candi_unique))
        candi_dict = {}
        for i in candi_sorted:
            candi_dict[i] = candidates.count(i)
        # print candi_dict # for test
        # print candi_sorted
        # print target
        result = self.findCombination(candi_sorted, candi_dict, target)
        if result == -1:
            return []
        solution_set = []
        for item in result:
            combination = []
            for i in range(0, len(item)):
                combination += item[i] * [candi_sorted[i]]
            solution_set.append(combination)
        return solution_set

    def findCombination(self, candi_sorted, candi_dict, tar):
        result = []
        k = candi_dict[candi_sorted[0]]
        # print candi_sorted
        # print k, tar
        while k >= 0:
            cur_tar = tar - candi_sorted[0] * k
            if cur_tar == 0:
                result.append([k])
            elif cur_tar < 0:
                pass
            elif len(candi_sorted) > 1:
                extra = self.findCombination(candi_sorted[1:], candi_dict, cur_tar)
                # print extra # for test
                if extra == -1:
                    pass
                else:
                    list_append = lambda x, y: x + y
                    result += map(list_append, [[k]]*len(extra), extra)
            k -= 1
        if len(result) > 0:
            return result
        else:
            return -1


if __name__ == '__main__':
    test_case = [
    [[1, 1, 2, 2, 4, 7, 9], 8],
    [[10, 1, 2,7,6,1,5], 8],
    [[10, 11, 12], 8]
    # [[2, 4, 5, 6, 7, 11], 11]
    ]
    for t in test_case:
        candi, targ = t
        combi = Solution().combinationSum2(candi, targ)
        print(combi)
