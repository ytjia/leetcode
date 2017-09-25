package leetcode;

import java.util.Arrays;

/**
 * @author ytjia created on 2017-09-21 15:43
 */
public class CombinationSum4 {

  /**
   * Given an integer array with all positive numbers and no duplicates, find the number of possible
   * combinations that add up to a positive integer target.
   * <p>
   * https://leetcode.com/problems/combination-sum-iv/description/
   */
  class Solution {

    public int combinationSum4(int[] nums, int target) {
      if (nums == null || nums.length == 0) {
        return 0;
      }
      Arrays.sort(nums);
      int[] dp = new int[target + 1];
      dp[0] = 1;
      for (int i = 1; i <= target; i++) {
        for (int j = 0; j < nums.length; j++) {
          if (i - nums[j] >= 0) {
            dp[i] += dp[i - nums[j]];
          } else {
            break;
          }
        }
      }
      return dp[target];
    }
  }

}
