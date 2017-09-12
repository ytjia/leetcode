package leetcode;

import java.util.Stack;

import leetcode.common.TreeNode;

/**
 * @author ytjia created on 2017-09-11 17:39
 */
public class FlattenBinaryTreetoLinkedList {

  /**
   * Given a binary tree, flatten it to a linked list in-place.
   * <p>
   * https://leetcode.com/problems/flatten-binary-tree-to-linked-list/description/
   */
  class Solution {

    public void flatten(TreeNode root) {
      if (root == null) {
        return;
      }

      Stack<TreeNode> stack = new Stack<>();
      stack.push(root);
      TreeNode preNode = new TreeNode(0);
      while (!stack.isEmpty()) {
        TreeNode curNode = stack.pop();
        preNode.left = null;
        preNode.right = curNode;
        if (curNode.right != null) {
          stack.push(curNode.right);
        }
        if (curNode.left != null) {
          stack.push(curNode.left);
        }
        preNode = curNode;
      }

    }
  }

}
