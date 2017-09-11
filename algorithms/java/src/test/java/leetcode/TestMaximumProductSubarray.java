package leetcode;

import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;

/**
 * @author ytjia created on 2017-09-10 19:22
 */
public class TestMaximumProductSubarray {

  MaximumProductSubarray.Solution solution;
  @Before
  public void setUp() throws Exception {
    MaximumProductSubarray maximumProductSubarray = new MaximumProductSubarray();
    solution = maximumProductSubarray.new Solution();
  }

  @Test
  public void testMaxProduct() throws Exception {
    Assert.assertEquals(1, solution.maxProduct(new int[]{1, 0}));
    Assert.assertEquals(0, solution.maxProduct(new int[]{-1, 0}));
    Assert.assertEquals(42, solution.maxProduct(new int[]{-4, -6, -7}));
    Assert.assertEquals(1, solution.maxProduct(new int[]{1}));
    Assert.assertEquals(-2, solution.maxProduct(new int[]{-2}));
  }

}
