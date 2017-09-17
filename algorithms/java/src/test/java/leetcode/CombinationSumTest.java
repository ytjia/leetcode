package leetcode;

import org.junit.Before;
import org.junit.Test;

/**
 * @author ytjia created on 2017-09-15 21:37
 */
public class CombinationSumTest {

  CombinationSum.Solution solution;

  @Before
  public void setUp() throws Exception {
    CombinationSum combinationSum = new CombinationSum();
    solution = combinationSum.new Solution();
  }

  @Test
  public void testC() throws Exception {
    int[] candidates = new int[]{2, 3, 4, 6, 7};
    System.out.println(solution.combinationSum(candidates, 7));
  }

}
