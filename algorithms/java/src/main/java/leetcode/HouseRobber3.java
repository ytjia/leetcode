package leetcode;

import leetcode.common.TreeNode;

/**
 * @author ytjia created on 2017-09-13 16:08
 */
public class HouseRobber3 {

  /**
   * The thief has found himself a new place for his thievery again. There is only one entrance to
   * this area, called the "root." Besides the root, each house has one and only one parent house.
   * After a tour, the smart thief realized that "all houses in this place forms a binary tree". It
   * will automatically contact the police if two directly-linked houses were broken into on the
   * same night.
   * <p>
   * Determine the maximum amount of money the thief can rob tonight without alerting the police.
   * <p>
   * https://leetcode.com/problems/house-robber-iii/description/
   */
  class Solution {

    public int rob(TreeNode root) {
      int[] result = robSub(root);
      return Math.max(result[0], result[1]);
    }

    private int[] robSub(TreeNode root) {
      if (root == null) {
        return new int[2];
      }
      int[] left = robSub(root.left);
      int[] right = robSub(root.right);
      int[] result = new int[2];
      result[0] = Math.max(left[0], left[1]) + Math.max(right[0], right[1]);
      result[1] = root.val + left[0] + right[0];

      return result;
    }
  }

}
