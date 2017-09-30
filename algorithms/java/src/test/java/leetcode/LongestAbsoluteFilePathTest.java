package leetcode;

import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;

/**
 * @author ytjia created on 2017-09-30 16:20
 */
public class LongestAbsoluteFilePathTest {

  LongestAbsoluteFilePath.Solution solution;

  @Before
  public void setUp() {
    LongestAbsoluteFilePath longestAbsoluteFilePath = new LongestAbsoluteFilePath();
    solution = longestAbsoluteFilePath.new Solution();
  }

  @Test
  public void testLengthLongestPath() {
    Assert.assertEquals(32, solution.lengthLongestPath(
        "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"));
  }
}
