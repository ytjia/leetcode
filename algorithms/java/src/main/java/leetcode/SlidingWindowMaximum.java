package leetcode;

import java.util.Arrays;

/**
 * @author ytjia created on 2017-10-11 16:37
 */
public class SlidingWindowMaximum {

  /**
   * Given an array nums, there is a sliding window of size k which is moving from the very left of
   * the array to the very right. You can only see the k numbers in the window. Each time the
   * sliding window moves right by one position.
   * <p>
   * https://leetcode.com/problems/sliding-window-maximum/description/
   */
  class Solution {

    public int[] maxSlidingWindow(int[] nums, int k) {
      if (null == nums || nums.length == 0) {
        return new int[0];
      }

      int numCnt = nums.length;
      int[] maxArr = new int[numCnt - k + 1];
      Arrays.fill(maxArr, Integer.MIN_VALUE);

      for (int i = numCnt - 1; i >= 0; i--) {
        for (int j = Math.max(0, i - (k - 1)); j <= i && j < maxArr.length; j++) {
          if (nums[i] > maxArr[j]) {
            maxArr[j] = nums[i];
          } else {
            break;
          }
        }
      }

      return maxArr;
    }
  }

}
