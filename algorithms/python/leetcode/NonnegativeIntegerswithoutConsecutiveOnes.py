# -*- coding: utf-8 -*-

# Authors: Y. Jia <ytjia.zju@gmail.com>


"""
Given a positive integer n, find the number of non-negative integers less than or equal to n, whose
binary representations do NOT contain consecutive ones.

https://leetcode.com/problems/non-negative-integers-without-consecutive-ones/description/
"""


class Solution(object):
    def findIntegers(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 1:
            return 2
        binary_bit_pos = self.find_binary_bit_pos(num)
        max_bit_pos = binary_bit_pos[-1]
        bit_cnt = self.stat_bit_cnt(max_bit_pos)

        less_than_bit_cnt = list()
        less_than_bit_cnt.append(0)
        for i in range(1, len(bit_cnt)):
            less_than_bit_cnt.append(less_than_bit_cnt[i - 1] + bit_cnt[i - 1])
        less_than_bit_cnt[0] = 1
        return self.find_integers_with_stat(binary_bit_pos, less_than_bit_cnt)

    def find_integers_with_stat(self, binary_bit_pos, less_than_bit_cnt):
        lens = len(binary_bit_pos)
        if lens == 1:
            return less_than_bit_cnt[binary_bit_pos[0]] + 1

        if binary_bit_pos[lens - 1] - binary_bit_pos[lens - 2] == 1:
            return less_than_bit_cnt[binary_bit_pos[lens - 1]] + less_than_bit_cnt[
                    binary_bit_pos[lens - 2]]
        else:
            return less_than_bit_cnt[binary_bit_pos[lens - 1]] + self.find_integers_with_stat(
                    binary_bit_pos[0:lens - 1], less_than_bit_cnt)

    def find_binary_bit_pos(self, num):
        binary_bit_pos = list()
        nnum = num
        if nnum == 0:
            return binary_bit_pos

        i = 0
        while nnum > 0:
            if nnum & 1 == 1:
                binary_bit_pos.append(i)
            i += 1
            nnum = nnum >> 1

        return binary_bit_pos

    def stat_bit_cnt(self, bit_pos_max):
        """
        x位二进制数 有多少个 integers without consecutive ones
        例如: 1位二进制数 有2个：0，1
        2位二进制数 有1个：2
        3位二进制数 有2个：4, 5
        :param bit_pos_max:
        :return:
        """
        w_c_ones_end_0_cnt = list()
        w_c_ones_end_1_cnt = list()
        w_c_ones_cnt = list()
        # 0, 1
        w_c_ones_end_0_cnt.append(1)
        w_c_ones_end_1_cnt.append(1)
        w_c_ones_cnt.append(2)
        # 2
        w_c_ones_end_0_cnt.append(1)
        w_c_ones_end_1_cnt.append(0)

        for i in range(1, bit_pos_max + 1):
            w_c_ones_end_0_cnt.append(w_c_ones_end_0_cnt[i] + w_c_ones_end_1_cnt[i])
            w_c_ones_end_1_cnt.append(w_c_ones_end_0_cnt[i])
            w_c_ones_cnt.append(w_c_ones_end_0_cnt[i] + w_c_ones_end_1_cnt[i])

        return w_c_ones_cnt
