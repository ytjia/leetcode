package leetcode;

/**
 * @author ytjia created on 2017-10-10 11:08
 */
public class JumpGame {

  /**
   * Given an array of non-negative integers, you are initially positioned at the first index of the
   * array. Each element in the array represents your maximum jump length at that position.
   * Determine if you are able to reach the last index.
   * <p>
   * https://leetcode.com/problems/jump-game/description/
   */
  class Solution {

    public boolean canJump(int[] nums) {
      if (null == nums || nums.length == 0) {
        return true;
      }

      int maxJumpIndex = nums[0];
      int i = 0;

      while (i <= maxJumpIndex) {
        maxJumpIndex = Math.max(maxJumpIndex, i + nums[i]);
        if (maxJumpIndex >= nums.length - 1) {
          return true;
        }
        ++i;
      }
      return false;
    }
  }

}
