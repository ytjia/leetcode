package leetcode;

import java.util.Arrays;

/**
 * @author ytjia created on 2017-09-30 16:37
 */
public class MaximalRectangle {

  /**
   * Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only
   * 1's and return its area.
   * <p>
   * https://leetcode.com/problems/maximal-rectangle/description/
   */
  class Solution {

    public int maximalRectangle(char[][] matrix) {
      if (null == matrix || matrix.length == 0 || matrix[0].length == 0) {
        return 0;
      }
      int m = matrix.length;
      int n = matrix[0].length;

      int[] left = new int[n];
      int[] right = new int[n];
      int[] height = new int[n];
      Arrays.fill(right, n);

      int maxArea = 0;
      for (int i = 0; i < m; i++) {
        int curLeft = 0;
        int curRight = n;
        for (int j = n - 1; j >= 0; j--) {
          if (matrix[i][j] == '1') {
            // update right
            right[j] = Math.min(right[j], curRight);
          } else {
            right[j] = n;
            curRight = j;
          }
        }
        for (int j = 0; j < n; j++) {
          if (matrix[i][j] == '1') {
            // update height
            height[j]++;
            // update left
            left[j] = Math.max(left[j], curLeft);
          } else {
            height[j] = 0;
            left[j] = 0;
            curLeft = j + 1;
          }
          // update maxArea
          maxArea = Math.max(maxArea, (right[j] - left[j]) * height[j]);
        }
      }

      return maxArea;
    }
  }

}
