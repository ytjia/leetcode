package leetcode;

/**
 * @author ytjia created on 2017-09-13 15:47
 */
public class CountingBits {

  /**
   * Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate
   * the number of 1's in their binary representation and return them as an array.
   * <p>
   * https://leetcode.com/problems/counting-bits/description/
   */
  class Solution {

    public int[] countBits(int num) {
      int[] bitsCnt = new int[num + 1];
      bitsCnt[0] = 0;
      for (int i = 1; i < num + 1; i++) {
        bitsCnt[i] = bitsCnt[i >> 1] + i % 2;
      }

      return bitsCnt;
    }
  }

}
