package leetcode;

import leetcode.common.TreeNode;

/**
 * @author ytjia created on 2017-09-12 23:07
 */
public class InvertBinaryTree {

  /**
   * Invert a binary tree.
   * <p>
   * https://leetcode.com/problems/invert-binary-tree/description/
   */
  class Solution {

    public TreeNode invertTree(TreeNode root) {
      if (root == null || (root.left == null && root.right == null)) {
        return root;
      }

      TreeNode node = root.left;
      root.left = invertTree(root.right);
      root.right = invertTree(node);
      return root;
    }
  }

}
