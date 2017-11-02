package leetcode;

/**
 * @author ytjia created on 2017-10-30 19:15
 */
public class RotateImage {

  /**
   * You are given an n x n 2D matrix representing an image.
   * <p>
   * Rotate the image by 90 degrees (clockwise).
   * <p>
   * https://leetcode.com/problems/rotate-image/description/
   */
  class Solution {

    public void rotate(int[][] matrix) {
      if (null == matrix || matrix.length == 0 || matrix.length != matrix[0].length) {
        return;
      }

      int toMove;
      int n = matrix.length;
      int begin = 0;
      // 逐层递归
      while (begin < (n + 1) / 2) {
        int end = n - 1 - begin;
        int j = begin;
        // 层内逐元素替换
        for (int i = begin; i < end; ++i) {
          int cnt = 0;
          toMove = matrix[i][j];
          // 一个元素带来四次移动
          while (cnt < 4) {
            int t = matrix[j][n - 1 - i];
            matrix[j][n - 1 - i] = toMove;
            toMove = t;
            int tmp = j;
            j = n - 1 - i;
            i = tmp;
            ++cnt;
          }
        }
        ++begin;
      }

    }
  }

}
