package leetcode;

/**
 * @author ytjia created on 2017-09-21 16:28
 */
public class Searcha2DMatrix2 {

  /**
   * Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the
   * following properties:
   * <p>
   * Integers in each row are sorted in ascending from left to right. Integers in each column are
   * sorted in ascending from top to bottom.
   * <p>
   * https://leetcode.com/problems/search-a-2d-matrix-ii/description/
   */
  class Solution {

    public boolean searchMatrix(int[][] matrix, int target) {
      if (matrix == null || matrix.length == 0 || matrix[0].length == 0) {
        return false;
      }
      int i = 0;
      int j = matrix[0].length - 1;
      while (i < matrix.length && j >= 0) {
        int cur = matrix[i][j];
        if (cur == target) {
          return true;
        } else if (cur > target) {
          j--;
        } else {
          i++;
        }
      }

      return false;
    }
  }

}
