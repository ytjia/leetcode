package leetcode;

import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;

import java.util.ArrayList;
import java.util.List;

/**
 * @author ytjia created on 2017-09-10 17:30
 */
public class TestSmallestRange {

  private SmallestRange.Solution solution;

  @Before
  public void setUp() throws Exception {
    SmallestRange smallestRange = new SmallestRange();
    solution = smallestRange.new Solution();
  }


  @Test
  public void testSmallestRange() throws Exception {
    List<List<Integer>> numsList = new ArrayList<List<Integer>>();
    List<Integer> nums1 = new ArrayList<Integer>();
    nums1.add(1);
    nums1.add(2);
    numsList.add(nums1);

    int[] smallestRange = new int[]{1, 1};
    Assert.assertArrayEquals(smallestRange, solution.smallestRange(numsList));
  }
}
