package leetcode;

/**
 * @author ytjia created on 2017-09-08 16:26
 */
public class ContainerWithMostWater {

  /**
   * Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i,
   * ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
   * Find two lines, which together with x-axis forms a container, such that the container contains
   * the most water.
   * <p>
   * Note: You may not slant the container and n is at least 2.
   * <p>
   * https://leetcode.com/problems/container-with-most-water/description/
   */
  class Solution {

    public int maxArea(int[] height) {
      int pointerL = 0;
      int pointerR = height.length - 1;
      int maxArea = 0;
      while (pointerL < pointerR) {
        if (height[pointerL] <= height[pointerR]) {
          maxArea = Math.max(maxArea, height[pointerL] * (pointerR - pointerL));
          pointerL++;
        } else {
          maxArea = Math.max(maxArea, height[pointerR] * (pointerR - pointerL));
          pointerR--;
        }
      }

      return maxArea;
    }
  }

}
