package leetcode;

/**
 * @author ytjia created on 2017-09-19 15:24
 */
public class SearchforaRange {

  /**
   * Given an array of integers sorted in ascending order, find the starting and ending position of
   * a given target value.
   * <p>
   * Your algorithm's runtime complexity must be in the order of O(log n).
   * <p>
   * If the target is not found in the array, return [-1, -1].
   * <p>
   * https://leetcode.com/problems/search-for-a-range/description/
   */
  class Solution {

    public int[] searchRange(int[] nums, int target) {
      if (nums == null || nums.length == 0) {
        return new int[]{-1, -1};
      }
      int leftInd = bSearch(nums, 0, nums.length, target, true);
      if (leftInd == -1) {
        return new int[]{-1, -1};
      } else {
        int rightInd = bSearch(nums, 0, nums.length, target, false);
        return new int[]{leftInd, rightInd};
      }
    }

    private int bSearch(int[] nums, int start, int end, int target, boolean left) {
      if (start >= end) {
        return -1;
      }
      int mid = start + (end - start) / 2;
      if (nums[mid] > target) {
        return bSearch(nums, start, mid, target, left);
      } else if (nums[mid] < target) {
        return bSearch(nums, mid + 1, end, target, left);
      } else {
        if (left) {
          if (mid == 0 || nums[mid - 1] < target) {
            return mid;
          } else {
            return bSearch(nums, start, mid, target, left);
          }
        } else {
          if (mid == nums.length - 1 || nums[mid + 1] > target) {
            return mid;
          } else {
            return bSearch(nums, mid + 1, end, target, left);
          }
        }
      }
    }
  }

}
