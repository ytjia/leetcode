# -*- coding: utf-8 -*-

# Authors: Y. Jia <ytjia.zju@gmail.com>

"""
https://leetcode.com/problems/the-skyline-problem/description/
"""

from heapq import heappop, heappush


class Hist(object):
    def __init__(self, h):
        # begin from l until r
        self.l = h[0]
        self.r = h[1]
        self.h = h[2]

    def __eq__(self, other):
        return self.l == other.l and self.r == other.r and self.h == other.h

    def to_list(self):
        return [self.l, self.r, self.h]


class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        skyline = [[-1, 0]]
        critical_points = set([b[0] for b in buildings] + [b[1] for b in buildings])
        live_bs = list()

        i = 0
        for point in sorted(critical_points):
            while i < len(buildings) and buildings[i][0] <= point:
                heappush(live_bs, (-buildings[i][2], buildings[i][1]))
                i += 1

            while live_bs and live_bs[0][1] <= point:
                heappop(live_bs)

            max_h = -live_bs[0][0] if live_bs else 0
            if max_h != skyline[-1][1]:
                skyline.append([point, max_h])

        return skyline[1:]

    def getSkyline2(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        b_cnt = len(buildings)
        skyline = list()
        if b_cnt == 0:
            return skyline
        hist_list = list()
        hist_0 = Hist(buildings[0])
        if hist_0.l > 0:
            hist_list.append(Hist([0, hist_0.l, 0]))
        hist_list.append(hist_0)

        for i in range(1, b_cnt):
            hist_t = Hist(buildings[i])
            t_l_index = self.lie_in(hist_list, hist_t.l)
            t_r_index = self.lie_in(hist_list, hist_t.r)

            if t_l_index is None:
                if hist_list[-1].r == hist_t.l:
                    if hist_list[-1].h == hist_t.h:
                        hist_list[-1] = Hist([hist_list[-1].l, hist_t.r, hist_t.h])
                    else:
                        hist_list.append(hist_t)
                else:
                    hist_list.append(Hist([hist_list[-1].r, hist_t.l, 0]))
                    hist_list.append(hist_t)
                continue
            if t_r_index is None:
                t_r_index = len(hist_list)

            new_hist_list = list()
            new_hist_list.extend(hist_list[0:t_l_index])
            if t_l_index == t_r_index:
                lied_hist = hist_list[t_l_index]
                if hist_t.h <= lied_hist.h:
                    new_hist_list.append(lied_hist)
                else:
                    if hist_t.l > lied_hist.l:
                        new_hist_list.append(Hist([lied_hist.l, hist_t.l, lied_hist.h]))
                    new_hist_list.append(hist_t)
                    new_hist_list.append(Hist([hist_t.r, lied_hist.r, lied_hist.h]))
            else:
                # handle hist_t left boundary
                l_lied_hist = hist_list[t_l_index]
                if hist_t.h <= l_lied_hist.h:
                    new_hist_list.append(l_lied_hist)
                else:
                    if hist_t.l > l_lied_hist.l:
                        new_hist_list.append(Hist([l_lied_hist.l, hist_t.l, l_lied_hist.h]))
                    new_hist_list.append(Hist([hist_t.l, l_lied_hist.r, hist_t.h]))

                # handle middle area
                for j in range(t_l_index + 1, t_r_index):
                    cur_hist = hist_list[j]
                    if hist_t.h < cur_hist.h:
                        new_hist_list.append(cur_hist)
                    else:
                        if new_hist_list[-1].h == hist_t.h:
                            new_hist_list[-1] = Hist([new_hist_list[-1].l, cur_hist.r, hist_t.h])
                        else:
                            new_hist_list.append(Hist([cur_hist.l, cur_hist.r, hist_t.h]))

                # handle hist_t right boundary
                if t_r_index == len(hist_list):
                    if hist_t.r > new_hist_list[-1].r:
                        if new_hist_list[-1].h == hist_t.h:
                            new_hist_list[-1] = Hist([new_hist_list[-1].l, hist_t.r, hist_t.h])
                        else:
                            new_hist_list.append(Hist([new_hist_list[-1].r, hist_t.r, hist_t.h]))
                else:
                    r_lied_hist = hist_list[t_r_index]
                    if hist_t.h < r_lied_hist.h:
                        new_hist_list.append(r_lied_hist)
                    elif hist_t.h == r_lied_hist.h:
                        if new_hist_list[-1].h == hist_t.h:
                            new_hist_list[-1] = Hist([new_hist_list[-1].l, r_lied_hist.r, hist_t.h])
                        else:
                            new_hist_list.append(r_lied_hist)
                    else:
                        if hist_t.r > r_lied_hist.l:
                            if new_hist_list[-1].h == hist_t.h:
                                new_hist_list[-1] = Hist([new_hist_list[-1].l, hist_t.r, hist_t.h])
                            else:
                                new_hist_list.append(Hist([r_lied_hist.l, hist_t.r, hist_t.h]))
                            new_hist_list.append(Hist([hist_t.r, r_lied_hist.r, r_lied_hist.h]))
                        else:
                            new_hist_list.append(r_lied_hist)

            if t_r_index + 1 < len(hist_list):
                new_hist_list.extend(hist_list[t_r_index + 1:])

            hist_list = new_hist_list

        if hist_list[0].h > 0:
            skyline.append([hist_list[0].l, hist_list[0].h])
        for i in range(1, len(hist_list)):
            skyline.append([hist_list[i].l, hist_list[i].h])

        skyline.append([hist_list[-1].r, 0])

        return skyline

    def lie_in(self, arr, target, begin=None, end=None):
        """

        :param arr: array or list of hist
        :param target:
        :param begin:
        :param end:
        :return:
        """
        if begin is None:
            begin = 0
        if end is None:
            end = len(arr) - 1
        if begin > end:
            return None
        elif begin == end:
            if arr[begin].l <= target < arr[begin].r:
                return begin
            else:
                return None

        mid = begin + (end - begin) / 2
        if arr[mid].l <= target < arr[mid].r:
            return mid
        elif arr[mid].r <= target:
            return self.lie_in(arr, target, mid + 1, end)
        else:
            return self.lie_in(arr, target, begin, mid - 1)
