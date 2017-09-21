package leetcode;

/**
 * @author ytjia created on 2017-09-20 19:25
 */
public class MedianofTwoSortedArrays {

  /**
   * There are two sorted arrays nums1 and nums2 of size m and n respectively.
   * <p>
   * Find the median of the two sorted arrays. The overall run time complexity should be O(log
   * (m+n)).
   * <p>
   * https://leetcode.com/problems/median-of-two-sorted-arrays/description/
   */
  class Solution {

    private static final double ERROR_VALUE = -1.0;

    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
      if (nums1 == null && nums2 == null) {
        return ERROR_VALUE;
      } else if (nums1 == null || nums1.length == 0) {
        return findMedianSortedArray(nums2);
      } else if (nums2 == null || nums2.length == 0) {
        return findMedianSortedArray(nums1);
      }
      int m = nums1.length;
      int n = nums2.length;
      if (m < n) {
        return findMedianSortedArrays(nums2, nums1);
      }
      int low2 = 0;
      int high2 = n * 2;
      while (low2 <= high2) {
        int cut2 = (low2 + high2) / 2;
        int cut1 = m + n - cut2;
        int L1 = (cut1 == 0) ? Integer.MIN_VALUE : nums1[(cut1 - 1) / 2];
        int L2 = (cut2 == 0) ? Integer.MIN_VALUE : nums2[(cut2 - 1) / 2];
        int R1 = (cut1 == m * 2) ? Integer.MAX_VALUE : nums1[cut1 / 2];
        int R2 = (cut2 == n * 2) ? Integer.MAX_VALUE : nums2[cut2 / 2];
        if (L1 > R2) {
          low2 = cut2 + 1;
        } else if (L2 > R1) {
          high2 = cut2 - 1;
        } else {
          return (Math.max(L1, L2) + Math.min(R1, R2)) / 2.0;
        }
      }
      return ERROR_VALUE;
    }


    private double findMedianSortedArray(int[] nums) {
      int lens = nums.length;
      if (lens == 0) {
        return ERROR_VALUE;
      }
      int mid = lens >> 1;
      if (lens % 2 == 0) {
        return (nums[mid - 1] + nums[mid]) / 2.0;
      } else {
        return nums[mid];
      }
    }
  }

}
