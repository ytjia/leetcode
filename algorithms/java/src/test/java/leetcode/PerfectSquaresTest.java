package leetcode;

import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;

/**
 * @author ytjia created on 2017-09-10 20:25
 */
public class PerfectSquaresTest {

  PerfectSquares.Solution solution;
  @Before
  public void setUp() throws Exception {
    PerfectSquares perfectSquares = new PerfectSquares();
    solution = perfectSquares.new Solution();
  }

  @Test
  public void testNumSquares() throws Exception {
    Assert.assertEquals(3, solution.numSquares(12));
    Assert.assertEquals(2, solution.numSquares(13));
  }

}
