package leetcode;

import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;

/**
 * @author ytjia created on 2017-09-14 11:50
 */
public class LongestPalindromicSubstringTest {

  LongestPalindromicSubstring.Solution solution;

  @Before
  public void setUp() throws Exception {
    LongestPalindromicSubstring longestPalindromicSubstring = new LongestPalindromicSubstring();
    solution = longestPalindromicSubstring.new Solution();
  }

  @Test
  public void testLongestPalindrome() throws Exception {
    Assert.assertEquals("bab", solution.longestPalindrome("bbabacc"));
    Assert.assertEquals("b", solution.longestPalindrome("b"));
    Assert.assertEquals("bbb", solution.longestPalindrome("bbb"));
  }

}
