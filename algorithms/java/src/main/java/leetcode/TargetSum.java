package leetcode;

/**
 * @author ytjia created on 2017-09-17 16:35
 */
public class TargetSum {

  /**
   * You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2
   * symbols + and -. For each integer, you should choose one from + and - as its new symbol.
   * <p>
   * Find out how many ways to assign symbols to make sum of integers equal to target S.
   * <p>
   * https://leetcode.com/problems/target-sum/description/
   */
  class Solution {

    public int findTargetSumWays(int[] nums, int S) {
      return backTrack(nums, 0, S);
    }

    private int backTrack(int[] nums, int numInd, int target) {
      if (numInd >= nums.length) {
        if (target == 0) {
          return 1;
        } else {
          return 0;
        }
      }
      return backTrack(nums, numInd + 1, target - nums[numInd]) +
             backTrack(nums, numInd + 1, target + nums[numInd]);
    }
  }

}
