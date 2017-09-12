package leetcode;

import java.util.Arrays;
import java.util.List;

/**
 * @author ytjia created on 2017-09-11 18:08
 */
public class CountofSmallerNumbersAfterSelf {

  /**
   * You are given an integer array nums and you have to return a new counts array. The counts array
   * has the property where counts[i] is the number of smaller elements to the right of nums[i].
   * <p>
   * https://leetcode.com/problems/count-of-smaller-numbers-after-self/description/
   */
  class Solution {

    public List<Integer> countSmaller(int[] nums) {
      int numCnt = nums.length;
      Integer[] statArr = new Integer[numCnt];
      BSTNode root = null;
      for (int i = numCnt - 1; i >= 0; i--) {
        root = updateBST(root, nums[i], i, 0, statArr);
      }

      return Arrays.asList(statArr);
    }

    public BSTNode updateBST(BSTNode root, int num, int index, int preSum, Integer[] statArr) {
      if (root == null) {
        root = new BSTNode(num, 0);
        statArr[index] = preSum;
      } else if (root.val == num) {
        root.dup += 1;
        statArr[index] = root.leftChildCnt + preSum;
      } else if (root.val < num) {
        root.right =
            updateBST(root.right, num, index, preSum + root.leftChildCnt + root.dup, statArr);
      } else {
        root.leftChildCnt += 1;
        root.left = updateBST(root.left, num, index, preSum, statArr);
      }
      return root;
    }
  }

  class BSTNode {

    int val, leftChildCnt, dup = 1;
    BSTNode left, right;

    public BSTNode(int val, int leftChildCnt) {
      this.val = val;
      this.leftChildCnt = leftChildCnt;
    }
  }

}
