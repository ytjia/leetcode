package leetcode;

/**
 * Accepted
 * https://leetcode.com/problems/factorial-trailing-zeroes/
 * Created by ytjia on 15/8/12.
 */
public class FactorialTrailingZeroes {

  public class Solution {

    public int trailingZeroes(int n) {
      int trailingZeroNum = 0;
      while (n >= 5) {
        trailingZeroNum += n / 5;
        n = n / 5;
      }

      return trailingZeroNum;
    }
  }

}
