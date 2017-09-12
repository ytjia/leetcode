package leetcode;

/**
 * @author ytjia created on 2017-09-11 13:36
 */
public class ProductofArrayExceptSelf {

  /**
   * Given an array of n integers where n > 1, nums, return an array output such that output[i] is
   * equal to the product of all the elements of nums except nums[i].
   * <p>
   * Solve it without division and in O(n).
   * <p>
   * https://leetcode.com/problems/product-of-array-except-self/description/
   */
  class Solution {

    public int[] productExceptSelf(int[] nums) {
      int numCnt = nums.length;
      int[] productExcpSelf = new int[numCnt];

      productExcpSelf[0] = 1;

      for (int i = 1; i < numCnt; i++) {
        productExcpSelf[i] = productExcpSelf[i - 1] * nums[i - 1];
      }
      int right = 1;
      for (int i = numCnt - 1; i >= 0; i--) {
        productExcpSelf[i] *= right;
        right *= nums[i];
      }

      return productExcpSelf;
    }

    public int[] productExceptSelfHighSpace(int[] nums) {
      int numCnt = nums.length;
      int[] leftSum = new int[numCnt];
      int[] rightSum = new int[numCnt];
      int[] productExcpSelf = new int[numCnt];

      leftSum[0] = 1;
      rightSum[numCnt - 1] = 1;
      for (int i = 1; i < numCnt; i++) {
        leftSum[i] = leftSum[i - 1] * nums[i - 1];
        rightSum[numCnt - 1 - i] = rightSum[numCnt - i] * nums[numCnt - i];
      }
      for (int i = 0; i < numCnt; i++) {
        productExcpSelf[i] = leftSum[i] * rightSum[i];
      }

      return productExcpSelf;
    }

  }
}
