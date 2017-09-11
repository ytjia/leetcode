package leetcode;

import java.util.Stack;

import leetcode.common.TreeNode;

/**
 * @author ytjia created on 2017-09-10 16:50
 */
public class KthSmallestElementinaBST {


  /**
   * Given a binary search tree, write a function kthSmallest to find the kth smallest element in
   * it.
   * <p>
   * https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/
   */
  class Solution {

    public int kthSmallest(TreeNode root, int k) {
      Stack<TreeNode> stack = new Stack<TreeNode>();
      int counter = 0;
      int kthSmallest = 0;
      while (root != null || !stack.empty()) {
        while (root != null) {
          stack.push(root);
          root = root.left;
        }
        root = stack.pop();
        if (++counter == k) {
          kthSmallest = root.val;
        }
        root = root.right;
      }

      return kthSmallest;
    }
  }

}
