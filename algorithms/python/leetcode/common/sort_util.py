# -*- coding: utf-8 -*-

# Authors: Y. Jia <ytjia.zju@gmail.com>

import copy


def binary_search(arr, target, arr_sorted=False):
    c_arr = copy.copy(arr)
    if not arr_sorted:
        c_arr.sort()
    lens = len(arr)
    if lens == 0:
        return False
    elif lens == 1:
        return arr[0] == target
    i = 0
    j = lens

    mid = i + (j - i) / 2
    if arr[mid] == target:
        return True
    elif arr[mid] < target:
        return binary_search(arr[mid + 1:], target, arr_sorted)
    else:
        return binary_search(arr[:mid], target, arr_sorted)
