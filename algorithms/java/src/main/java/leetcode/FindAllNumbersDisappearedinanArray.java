package leetcode;

import java.util.LinkedList;
import java.util.List;

/**
 * @author ytjia created on 2017-09-13 12:11
 */
public class FindAllNumbersDisappearedinanArray {

  /**
   * Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice
   * and others appear once.
   * <p>
   * Find all the elements of [1, n] inclusive that do not appear in this array.
   * <p>
   * Could you do it without extra space and in O(n) runtime? You may assume the returned list does
   * not count as extra space.
   * <p>
   * https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/
   */
  class Solution {

    public List<Integer> findDisappearedNumbers(int[] nums) {
      List<Integer> disappearedNums = new LinkedList<>();
      if (nums == null) {
        return disappearedNums;
      }
      int tmp;
      for (int i = 0; i < nums.length; i++) {
        while (nums[i] != i + 1 && nums[nums[i] - 1] != nums[i]) {
          tmp = nums[i];
          nums[i] = nums[nums[i] - 1];
          nums[tmp - 1] = tmp;
        }
      }
      for (int i = 0; i < nums.length; i++) {
        if (nums[i] != i + 1) {
          disappearedNums.add(i + 1);
        }
      }

      return disappearedNums;
    }
  }

}
