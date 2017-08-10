#!/usr/bin python
# -*- coding: utf-8 -*-

"""
Say you have an array for which the ith element is the price of a
given stock on day i.
Design an algorithm to find the maximum profit. You may complete as
many transactions as you like (ie, buy one and sell one share of the
stock multiple times). However, you may not engage in multiple
transactions at the same time (ie, you must sell the stock before
you buy again).
https://oj.leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
"""

class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if len(prices) == 0:
            return 0
        cur = prices[0]
        tot = 0
        for p in prices:
            if p <= cur:
                cur = p
            else:
                tot += p - cur
                cur = p
        return tot

if __name__ == '__main__':
    test_case = [
        [1, 5, 3, 7, 8, 11],
        [4, 5, 1, 0]
        ]
    for test_s in test_case:
        subs = Solution().maxProfit(test_s)
        print(subs)
