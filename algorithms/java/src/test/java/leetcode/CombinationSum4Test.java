package leetcode;

import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;

/**
 * @author ytjia created on 2017-09-15 21:37
 */
public class CombinationSum4Test {

  CombinationSum4.Solution solution;

  @Before
  public void setUp() throws Exception {
    CombinationSum4 combinationSum4 = new CombinationSum4();
    solution = combinationSum4.new Solution();
  }

  @Test
  public void testCombinationSum4() throws Exception {
    int[] candidates = new int[]{1, 2, 3};
    Assert.assertEquals(7, solution.combinationSum4(candidates, 4));
  }

}
