package leetcode;

import java.util.Arrays;

/**
 * @author ytjia created on 2017-09-08 16:05
 */
public class MajorityElement {

  /**
   * Given an array of size n, find the majority element. The majority element is the element that
   * appears more than ⌊ n/2 ⌋ times.
   * <p>
   * You may assume that the array is non-empty and the majority element always exist in the array.
   * <p>
   * https://leetcode.com/problems/majority-element/description/
   */
  class Solution {

    public int majorityElement(int[] nums) {
      Arrays.sort(nums);
      return nums[nums.length / 2];
    }
  }

}


