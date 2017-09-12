package leetcode;

import leetcode.common.TreeNode;

/**
 * @author ytjia created on 2017-09-12 16:45
 */
public class SubtreeofAnotherTree {

  /**
   * Given two non-empty binary trees s and t, check whether tree t has exactly the same structure
   * and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all
   * of this node's descendants. The tree s could also be considered as a subtree of itself.
   * <p>
   * https://leetcode.com/problems/subtree-of-another-tree/description/
   */
  class Solution {

    public boolean isSubtree(TreeNode s, TreeNode t) {
      return isSameTree(s, t) || (s != null && (isSubtree(s.left, t) || isSubtree(s.right, t)));

    }

    public boolean isSameTree(TreeNode s, TreeNode t) {
      if (t == null && s == null) {
        return true;
      }
      if (s == null || t == null) {
        return false;
      }
      return s.val == t.val && isSameTree(s.left, t.left) && isSameTree(s.right, t.right);

    }
  }

}
