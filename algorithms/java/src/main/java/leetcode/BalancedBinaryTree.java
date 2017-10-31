package leetcode;

import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.Map;

import leetcode.common.TreeNode;

/**
 * @author ytjia created on 2017-10-30 17:38
 */
public class BalancedBinaryTree {

  /**
   * Given a binary tree, determine if it is height-balanced.
   * <p>
   * For this problem, a height-balanced binary tree is defined as a binary tree in which the depth
   * of the two subtrees of every node never differ by more than 1.
   * <p>
   * https://leetcode.com/problems/balanced-binary-tree/description/
   */
  class Solution {

    private static final int LEAF_HEIGHT = 0;
    private static final int UNBALANCED_STATUS = -1;

    public boolean isBalanced(TreeNode root) {
      if (null == root) {
        return true;
      }
      return dfsHeight(root) != UNBALANCED_STATUS;
    }

    private int dfsHeight(TreeNode root) {
      if (null == root) {
        return LEAF_HEIGHT;
      }

      int leftChildHeight = dfsHeight(root.left);
      if (leftChildHeight == UNBALANCED_STATUS) {
        return UNBALANCED_STATUS;
      }
      int rightChildHeight = dfsHeight(root.right);
      if (rightChildHeight == UNBALANCED_STATUS) {
        return UNBALANCED_STATUS;
      }

      if (Math.abs(leftChildHeight - rightChildHeight) > 1) {
        return UNBALANCED_STATUS;
      }

      return Math.max(leftChildHeight, rightChildHeight) + 1;
    }

    private boolean buildHeightMap(TreeNode root, Map<TreeNode, Integer> heightMap) {
      if (heightMap.containsKey(root)) {
        return true;
      }
      int leftChildHeight = LEAF_HEIGHT;
      int rightChildHeight = LEAF_HEIGHT;

      if (null != root.left) {
        if (!buildHeightMap(root.left, heightMap)) {
          return false;
        }
        leftChildHeight = heightMap.get(root.left);
      }
      if (null != root.right) {
        if (!buildHeightMap(root.right, heightMap)) {
          return false;
        }
        rightChildHeight = heightMap.get(root.right);
      }

      if (Math.abs(leftChildHeight - rightChildHeight) > 1) {
        return false;
      }
      heightMap.put(root, Math.max(leftChildHeight, rightChildHeight) + 1);
      return true;
    }
  }
}
