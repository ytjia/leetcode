package leetcode;

import leetcode.common.TreeNode;

/**
 * @author ytjia created on 2017-09-12 23:12
 */
public class DiameterofBinaryTree {

  /**
   * Given a binary tree, you need to compute the length of the diameter of the tree. The diameter
   * of a binary tree is the length of the longest path between any two nodes in a tree. This path
   * may or may not pass through the root.
   * <p>
   * https://leetcode.com/problems/diameter-of-binary-tree/description/
   */
  class Solution {

    int diameter = 0;

    public int diameterOfBinaryTree(TreeNode root) {
      depthOfBinaryTree(root);
      return diameter;
    }

    public int depthOfBinaryTree(TreeNode root) {
      if (root == null) {
        return 0;
      } else {
        int leftDepth = depthOfBinaryTree(root.left);
        int rightDepth = depthOfBinaryTree(root.right);
        diameter = Math.max(diameter, rightDepth + leftDepth);
        return Math.max(leftDepth, rightDepth) + 1;
      }
    }
  }

}
