package leetcode;

import java.util.Stack;

import leetcode.common.TreeNode;

/**
 * @author ytjia created on 2017-10-11 15:12
 */
public class ConvertBSTtoGreaterTree {

  /**
   * Definition for a binary tree node.
   * public class TreeNode {
   *     int val;
   *     TreeNode left;
   *     TreeNode right;
   *     TreeNode(int x) { val = x; }
   * }
   */


  /**
   * Given a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the
   * original BST is changed to the original key plus sum of all keys greater than the original key
   * in BST.
   * <p>
   * https://leetcode.com/problems/convert-bst-to-greater-tree/description/
   */
  class Solution {

    public TreeNode convertBST(TreeNode root) {
      if (null == root) {
        return root;
      }

      int greaterSum = 0;
      Stack<TreeNode> stack = new Stack<>();
      TreeNode node = root;

      while (!stack.empty() || null != node) {
        while (null != node) {
          stack.push(node);
          node = node.right;
        }

        node = stack.pop();
        node.val += greaterSum;
        greaterSum = node.val;

        node = node.left;
      }

      return root;
    }
  }

}
