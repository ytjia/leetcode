package leetcode;

import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;

/**
 * @author ytjia created on 2017-09-15 19:26
 */
public class FriendCirclesTest {

  FriendCircles.Solution solution;

  @Before
  public void setUp() throws Exception {
    FriendCircles friendCircles = new FriendCircles();
    solution = friendCircles.new Solution();
  }

  @Test
  public void testC() throws Exception {
    int[] a = new int[] {1, 0, 0, 1};
    int[] b = new int[] {0, 1, 1, 0};
    int[] c = new int[] {0, 1, 1, 1};
    int[] d = new int[] {1, 0, 1, 1};
    int[][] m = new int[][] {a, b, c, c};

    Assert.assertEquals(1, solution.findCircleNum(m));
  }

}
