package leetcode;

import java.util.Arrays;

/**
 * @author ytjia created on 2017-10-11 15:34
 */
public class NextPermutation {

  /**
   * Implement next permutation, which rearranges numbers into the lexicographically next greater
   * permutation of numbers.
   * <p>
   * If such arrangement is not possible, it must rearrange it as the lowest possible order (ie,
   * sorted in ascending order).
   * <p>
   * The replacement must be in-place, do not allocate extra memory.
   * <p>
   * https://leetcode.com/problems/next-permutation/description/
   */
  class Solution {

    public void nextPermutation(int[] nums) {
      if (null == nums || nums.length <= 1) {
        return;
      }

      int numCnt = nums.length;
      int curMax = nums[numCnt - 1];
      for (int i = numCnt - 2; i >= 0; i--) {
        if (nums[i] >= curMax) {
          curMax = nums[i];
        } else {
          Arrays.sort(nums, i + 1, numCnt);
          for (int j = i + 1; j < numCnt; j++) {
            if (nums[j] > nums[i]) {
              swap(nums, i, j);
              break;
            }
          }
          Arrays.sort(nums, i + 1, numCnt);
          return;
        }
      }
      Arrays.sort(nums);
    }

    private void swap(int[] arr, int i, int j) {
      int tmp = arr[i];
      arr[i] = arr[j];
      arr[j] = tmp;
    }
  }

}
