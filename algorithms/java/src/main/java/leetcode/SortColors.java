package leetcode;

/**
 * @author ytjia created on 2017-09-25 17:14
 */
public class SortColors {

  /**
   * Given an array with n objects colored red, white or blue, sort them so that objects of the same
   * color are adjacent, with the colors in the order red, white and blue.
   * <p>
   * Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue
   * respectively.
   * <p>
   * https://leetcode.com/problems/sort-colors/description/
   */
  class Solution {

    public void sortColors(int[] nums) {
      if (null == nums || nums.length <= 1) {
        return;
      }

      int lens = nums.length;
      int zero = 0;
      int second = lens - 1;

      for (int i = 0; i <= second; i++) {
        while (nums[i] == 2 && i < second) {
          swap(nums, i, second--);
        }
        while (nums[i] == 0 && i > zero) {
          swap(nums, i, zero++);
        }
      }

    }

    private void swap(int[] nums, int i, int j) {
      int tmp = nums[i];
      nums[i] = nums[j];
      nums[j] = tmp;
    }
  }

}
