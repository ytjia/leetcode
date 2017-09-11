package leetcode;

/**
 * @author ytjia created on 2017-09-10 18:53
 */
public class MaximumProductSubarray {

  /**
   * Find the contiguous subarray within an array (containing at least one number) which has the
   * largest product.
   * <p>
   * https://leetcode.com/problems/maximum-product-subarray/description/
   */
  class Solution {

    public int maxProduct(int[] nums) {
      int maxProduct = nums[0];
      int curMaxProduct = nums[0];
      int curMinProduct = nums[0];

      for (int i = 1; i < nums.length; i++) {
        if (nums[i] < 0) {
          // swap
          int tmp = curMaxProduct;
          curMaxProduct = curMinProduct;
          curMinProduct = tmp;
        }
        curMaxProduct = Math.max(nums[i], curMaxProduct * nums[i]);
        curMinProduct = Math.min(nums[i], curMinProduct * nums[i]);

        maxProduct = Math.max(maxProduct, curMaxProduct);
      }

      return maxProduct;
    }
  }
}
