package leetcode;

import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;

/**
 * @author ytjia created on 2017-09-13 11:54
 */
public class MoveZerosTest {

  MoveZeroes.Solution solution;

  @Before
  public void setUp() throws Exception {
    MoveZeroes moveZeroes = new MoveZeroes();
    solution = moveZeroes.new Solution();
  }

  @Test
  public void testMoveZeros() throws Exception {
    int[] expected = new int[] {1, 0};
    solution.moveZeroes(expected);
    Assert.assertArrayEquals(expected, new int[] {1, 0});
  }

}
