# -*- coding: utf-8 -*-

# Authors: Y. Jia <ytjia.zju@gmail.com>



def binary_search(arr, target, begin=None, end=None):
    """

    :param arr:
    :param target:
    :param begin:
    :param end:
    :return:
    """
    if begin is None:
        begin = 0
    if end is None:
        end = len(arr) - 1
    if end < begin or end < 0:
        return False, None
    elif end == begin:
        if arr[end] == target:
            return True, end
        else:
            return False, None

    mid = begin + (end - begin) / 2
    if arr[mid] == target:
        return True, mid
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, end)
    else:
        return binary_search(arr, target, begin, mid - 1)
