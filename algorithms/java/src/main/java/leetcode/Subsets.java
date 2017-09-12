package leetcode;

import java.util.ArrayList;
import java.util.List;

/**
 * @author ytjia created on 2017-09-11 17:11
 */
public class Subsets {


  /**
   * Given a set of distinct integers, nums, return all possible subsets.
   * <p>
   * Note: The solution set must not contain duplicate subsets.
   * <p>
   * https://leetcode.com/problems/subsets/description/
   */
  class Solution {

    public List<List<Integer>> subsets(int[] nums) {
      return subsets(nums, 0, nums.length);
    }

    public List<List<Integer>> subsets(int[] nums, int start, int end) {
      List<List<Integer>> subsets = new ArrayList<>();
      if (start == end) {
        List<Integer> subset = new ArrayList<>();
        subsets.add(subset);
        return subsets;
      }

      List<List<Integer>> preSubsets = subsets(nums, start, end - 1);
      subsets.addAll(preSubsets);
      for (List<Integer> subset : preSubsets) {
        List<Integer> newSubset = new ArrayList<>(subset);
        newSubset.add(nums[end - 1]);
        subsets.add(newSubset);
      }

      return subsets;
    }
  }

}
