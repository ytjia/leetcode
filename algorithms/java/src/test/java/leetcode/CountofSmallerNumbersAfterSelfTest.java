package leetcode;

import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;

import java.util.ArrayList;
import java.util.List;

/**
 * @author ytjia created on 2017-09-12 14:32
 */
public class CountofSmallerNumbersAfterSelfTest {

  CountofSmallerNumbersAfterSelf.Solution solution;

  @Before
  public void setUp() throws Exception {
    CountofSmallerNumbersAfterSelf c = new CountofSmallerNumbersAfterSelf();
    solution = c.new Solution();
  }

  @Test
  public void testC() throws Exception {
    List<Integer> expected = new ArrayList<>();
    expected.add(3);
    expected.add(2);
    expected.add(0);
    expected.add(0);
    expected.add(0);
    int[] nums = new int[5];
    nums[0] = 7;
    nums[1] = 6;
    nums[2] = 3;
    nums[3] = 4;
    nums[4] = 9;
    Assert.assertArrayEquals(expected.toArray(), solution.countSmaller(nums).toArray());
  }
}
