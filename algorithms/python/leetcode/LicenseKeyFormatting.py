# -*- coding: utf-8 -*-

# Authors: Y. Jia <ytjia.zju@gmail.com>

"""
Now you are given a string S, which represents a software license key which we would like to
format. The string S is composed of alphanumerical characters and dashes. The dashes split the
alphanumerical characters within the string into groups. (i.e. if there are M dashes, the string is
split into M+1 groups). The dashes in the given string are possibly misplaced.

We want each group of characters to be of length K (except for possibly the first group, which
could be shorter, but still must contain at least one character). To satisfy this requirement, we
will reinsert dashes. Additionally, all the lower case letters in the string must be converted to
upper case.

So, you are given a non-empty string S, representing a license key to format, and an integer K. And
you need to return the license key formatted according to the description above.

https://leetcode.com/problems/license-key-formatting/description/
"""


class Solution(object):
    _ord_a = ord('a')
    _ord_z = ord('z')
    _offset = ord('A') - ord('a')

    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        length = len(S)
        i = length - 1
        j = 0
        transformed_list = list()
        while i >= 0:
            cur_char = S[i]
            if cur_char == '-':
                pass
            elif ord(cur_char) >= self._ord_a and ord(cur_char) <= self._ord_z:
                transformed_list.append(chr(ord(cur_char) + self._offset))
                j += 1
            else:
                transformed_list.append(cur_char)
                j += 1
            if j == K:
                transformed_list.append('-')
                j = 0
            i -= 1

        if len(transformed_list) > 0 and transformed_list[-1] == '-':
            del transformed_list[-1]
        transformed_list.reverse()
        return ''.join(transformed_list)


if __name__ == '__main__':
    print(Solution().licenseKeyFormatting("2-4A0r7-4k", 4))
