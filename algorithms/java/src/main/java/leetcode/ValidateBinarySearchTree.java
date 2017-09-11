package leetcode;

import leetcode.common.TreeNode;

/**
 * @author ytjia created on 2017-09-08 17:31
 */
public class ValidateBinarySearchTree {


  /**
   * Given a binary tree, determine if it is a valid binary search tree (BST).
   * <p>
   * Assume a BST is defined as follows:
   * <p>
   * The left subtree of a node contains only nodes with keys less than the node's key. The right
   * subtree of a node contains only nodes with keys greater than the node's key. Both the left and
   * right subtrees must also be binary search trees.
   * <p>
   * https://leetcode.com/problems/validate-binary-search-tree/description/
   */
  class Solution {

    public boolean isValidBST(TreeNode root) {
      if (root == null) {
        return true;
      }
      return checkValidBST(root).valid;

    }


    public ValidInfo checkValidBST(TreeNode root) {
      assert root != null;
      if (root.left == null && root.right == null) {
        return new ValidInfo(true, root.val, root.val);
      } else {
        if (root.left == null) {
          ValidInfo validInfo = checkValidBST(root.right);
          boolean status = validInfo.valid && (root.val < validInfo.min);
          return new ValidInfo(status, validInfo.max, root.val);
        } else {
          if (root.right == null) {
            ValidInfo validInfo = checkValidBST(root.left);
            boolean status = validInfo.valid && (root.val > validInfo.max);
            return new ValidInfo(status, root.val, validInfo.min);
          } else {
            ValidInfo leftValidInfo = checkValidBST(root.left);
            ValidInfo rightValidInfo = checkValidBST(root.right);
            boolean status = leftValidInfo.valid && rightValidInfo.valid &&
                             (leftValidInfo.max < root.val) && (root.val < rightValidInfo.min);
            return new ValidInfo(status, rightValidInfo.max, leftValidInfo.min);
          }
        }
      }
    }
  }

  class ValidInfo {

    int max;
    int min;
    boolean valid;

    ValidInfo(boolean valid, int max, int min) {
      this.valid = valid;
      this.max = max;
      this.min = min;
    }
  }
}
