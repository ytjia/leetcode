package leetcode;

import java.util.Arrays;

/**
 * @author ytjia created on 2017-09-19 18:51
 */
public class KthLargestElementinanArray {

  /**
   * Find the kth largest element in an unsorted array. Note that it is the kth largest element in
   * the sorted order, not the kth distinct element.
   * <p>
   * https://leetcode.com/problems/kth-largest-element-in-an-array/description/
   */
  class Solution {

    public int findKthLargest(int[] nums, int k) {
      Arrays.sort(nums);
      return nums[nums.length - k];
    }
  }

}
