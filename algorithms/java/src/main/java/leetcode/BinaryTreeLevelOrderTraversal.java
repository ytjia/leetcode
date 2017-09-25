package leetcode;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

import leetcode.common.TreeNode;

/**
 * @author ytjia created on 2017-09-21 15:13
 */
public class BinaryTreeLevelOrderTraversal {

  /**
   * Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to
   * right, level by level).
   * <p>
   * https://leetcode.com/problems/binary-tree-level-order-traversal/description/
   */
  class Solution {

    public List<List<Integer>> levelOrder(TreeNode root) {
      List<List<Integer>> levelTravel = new LinkedList<>();
      if (root == null) {
        return levelTravel;
      }
      List<List<TreeNode>> nodeList = new ArrayList<>();
      List<TreeNode> rootList = new ArrayList<>();
      List<Integer> rootValueList = new ArrayList<>();
      rootList.add(root);
      rootValueList.add(root.val);
      nodeList.add(rootList);
      levelTravel.add(rootValueList);
      int i = 0;
      while (i < nodeList.size()) {
        List<TreeNode> curList = nodeList.get(i);
        List<TreeNode> nextList = new ArrayList<>();
        List<Integer> nextValueList = new ArrayList<>();
        for (TreeNode node : curList) {
          if (node.left != null) {
            nextList.add(node.left);
            nextValueList.add(node.left.val);
          }
          if (node.right != null) {
            nextList.add(node.right);
            nextValueList.add(node.right.val);
          }
        }
        if (nextList.size() > 0) {
          nodeList.add(nextList);
          levelTravel.add(nextValueList);
        }
        i++;
      }

      return levelTravel;
    }
  }

}
