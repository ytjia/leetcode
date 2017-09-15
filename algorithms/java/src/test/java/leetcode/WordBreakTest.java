package leetcode;

import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;

import java.util.ArrayList;
import java.util.List;

/**
 * @author ytjia created on 2017-09-14 17:38
 */
public class WordBreakTest {

  WordBreak.Solution solution;

  @Before
  public void setUp() throws Exception {
    WordBreak wordBreak = new WordBreak();
    solution = wordBreak.new Solution();
  }

  @Test
  public void testWordBreak() throws Exception {
    List<String> dict = new ArrayList<>();
    dict.add("a");
    Assert.assertTrue(solution.wordBreak("aaa", dict));
  }

}
