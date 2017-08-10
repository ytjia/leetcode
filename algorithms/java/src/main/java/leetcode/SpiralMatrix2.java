package leetcode;

/**
 * Accepted!
 *
 * https://leetcode.com/problems/spiral-matrix-ii/
 * Created by ytjia on 15/12/28.
 */
public class SpiralMatrix2 {

  public class Solution {

    public int[][] generateMatrix(int n) {
      int[][] matrix = new int[n][n];
      int total = n*n;

      int i = 1;
      int r = 0;
      int c = 0;
      int step = 0;
      while (i <= total) {
        while (c + step < n) {
          matrix[r][c++] = i++;
        }
        c--;
        r++;

        while (r + step < n) {
          matrix[r++][c] = i++;
        }
        r--;
        c--;

        while (c >= step) {
          matrix[r][c--] = i++;
        }
        c++;
        r--;
        step++;

        while (r >= step) {
          matrix[r--][c] = i++;
        }
        r++;
        c++;
      }

      return matrix;
    }
  }

}
