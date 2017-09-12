package leetcode;

import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;

/**
 * @author ytjia created on 2017-09-12 16:18
 */
public class DecodeStringTest {

  DecodeString.Solution solution;

  @Before
  public void setUp() throws Exception {
    DecodeString decodeString = new DecodeString();
    solution = decodeString.new Solution();
  }

  @Test
  public void testDecodeString() throws Exception {
    Assert.assertEquals("aaa", solution.decodeString("3[a]"));
    Assert.assertEquals("aacaacaac", solution.decodeString("3[2[a]c]"));
    Assert.assertEquals("abccdbccd", solution.decodeString("a2[b2[c]d]"));
  }

}
