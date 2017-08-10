# -*- coding: utf-8 -*-

# Authors: Y. Jia <ytjia.zju@gmail.com>

import unittest

from .. import LicenseKeyFormatting


class test_LicenseKeyFormatting(unittest.TestCase):
    def test_LicenseKeyFormatting(self):
        solution = LicenseKeyFormatting.Solution()
        self.assertEqual(solution.licenseKeyFormatting("2-4A0r7-4k", 4), "24A0-R74K")
        self.assertEqual(solution.licenseKeyFormatting("2-4A0r7-4k", 3), "24-A0R-74K")
        self.assertEqual(solution.licenseKeyFormatting("--a-a-a-a--", 2), "AA-AA")
        self.assertEqual(solution.licenseKeyFormatting("---", 3), "")


if __name__ == '__main__':
    unittest.main()
