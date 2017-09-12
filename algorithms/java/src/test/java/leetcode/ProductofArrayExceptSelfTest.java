package leetcode;

import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;

import java.util.Arrays;

/**
 * @author ytjia created on 2017-09-11 16:58
 */
public class ProductofArrayExceptSelfTest {

  ProductofArrayExceptSelf.Solution solution;

  @Before
  public void setUp() throws Exception {
    ProductofArrayExceptSelf productofArrayExceptSelf = new ProductofArrayExceptSelf();
    solution = productofArrayExceptSelf.new Solution();
  }

  @Test
  public void testProductExceptSelf() throws Exception {
    int[] nums = new int[2];
    int[] expected = new int[2];
    Arrays.fill(nums, 1);
    Arrays.fill(expected, 1);
    Assert.assertArrayEquals(expected, solution.productExceptSelf(nums));
  }

}
