package leetcode;

/**
 * @author ytjia created on 2017-09-10 19:48
 */
public class PerfectSquares {

  /**
   * Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4,
   * 9, 16, ...) which sum to n.
   * <p>
   * https://leetcode.com/problems/perfect-squares/description/
   */
  class Solution {

    public int numSquares(int n) {
      if (n <= 0) {
        return 0;
      }
      int[] numSquareCnt = new int[n + 1];
      for (int i = 0; i <= n; i++) {
        numSquareCnt[i] = Integer.MAX_VALUE;
      }
      numSquareCnt[0] = 0;
      for (int i = 1; i <= n; i++) {
        for (int j = 1; j * j <= i; j++) {
          numSquareCnt[i] = Math.min(numSquareCnt[i], numSquareCnt[i - j * j] + 1);
        }
      }

      return numSquareCnt[n];
    }
  }

}
