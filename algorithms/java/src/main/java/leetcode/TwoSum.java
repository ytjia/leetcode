package leetcode;

import java.util.HashMap;
import java.util.Map;

/**
 * @author ytjia created on 2017-09-12 22:29
 */
public class TwoSum {

  /**
   * Given an array of integers, return indices of the two numbers such that they add up to a
   * specific target.
   * <p>
   * You may assume that each input would have exactly one solution, and you may not use the same
   * element twice.
   * <p>
   * https://leetcode.com/problems/two-sum/description/
   */
  class Solution {

    public int[] twoSum(int[] nums, int target) {
      Map<Integer, Integer> numIndexMap = new HashMap<>();
      int[] result = new int[2];

      for (int i = 0; i < nums.length; i++) {
        if (numIndexMap.containsKey(target - nums[i])) {
          result[0] = i;
          result[1] = numIndexMap.get(target - nums[i]);
          break;
        } else {
          numIndexMap.put(nums[i], i);
        }
      }

      return result;
    }
  }

}
