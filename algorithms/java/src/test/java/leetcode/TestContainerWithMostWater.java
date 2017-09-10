package leetcode;

import org.junit.Assert;
import org.junit.Test;

import leetcode.common.TreeNode;


/**
 * @author jiayitian created on 2017-09-08 18:00
 */
public class TestContainerWithMostWater {

  @Test
  public void isValidBST() {
    TreeNode root = new TreeNode(2);
    root.left = new TreeNode(1);
    root.right = new TreeNode(3);

    ValidateBinarySearchTree validateBinarySearchTree = new ValidateBinarySearchTree();
    ValidateBinarySearchTree.Solution solution = validateBinarySearchTree.new Solution();

    Assert.assertTrue(solution.isValidBST(root));
  }

}
