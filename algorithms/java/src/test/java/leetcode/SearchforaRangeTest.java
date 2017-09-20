package leetcode;

import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;

/**
 * @author ytjia created on 2017-09-19 18:16
 */
public class SearchforaRangeTest {

  SearchforaRange.Solution solution;

  @Before
  public void setUp() throws Exception {
    SearchforaRange searchforaRange = new SearchforaRange();
    solution = searchforaRange.new Solution();
  }

  @Test
  public void testSearchRange() throws Exception {
    Assert.assertArrayEquals(new int[]{-1, -1}, solution.searchRange(new int[]{1, 2, 3, 3, 4}, 5));
    Assert.assertArrayEquals(new int[]{2, 3}, solution.searchRange(new int[]{1, 2, 3, 3, 4}, 3));
  }

}
