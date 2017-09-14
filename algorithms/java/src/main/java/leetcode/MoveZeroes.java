package leetcode;

/**
 * @author ytjia created on 2017-09-13 00:11
 */
public class MoveZeroes {

  /**
   * Given an array nums, write a function to move all 0's to the end of it while maintaining the
   * relative order of the non-zero elements.
   * <p>
   * For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3,
   * 12, 0, 0].
   * <p>
   * https://leetcode.com/problems/move-zeroes/description/
   */
  class Solution {

    public void moveZeroes(int[] nums) {
      if (nums == null) {
        return;
      }
      int tmp;
      for (int cur = 0, lastNonZero = 0; cur < nums.length; cur++) {
        if (nums[cur] != 0) {
          tmp = nums[lastNonZero];
          nums[lastNonZero++] = nums[cur];
          nums[cur] = tmp;
        }
      }
    }
  }

}
