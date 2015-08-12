package leetcode;

import static org.junit.Assert.assertEquals;
import org.junit.Test;

/**
 * Created by ytjia on 15/8/12.
 */
public class TestFactorialTrailingZeros {

  @Test
  public void trailingZeroes() {
    FactorialTrailingZeroes f = new FactorialTrailingZeroes();
    FactorialTrailingZeroes.Solution s = f.new Solution();

    assertEquals(0, s.trailingZeroes(4));
    assertEquals(1, s.trailingZeroes(5));
    assertEquals(2, s.trailingZeroes(10));
    assertEquals(6, s.trailingZeroes(25));
  }
}
