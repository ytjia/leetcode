package leetcode;

import java.util.HashSet;
import java.util.List;
import java.util.Set;

/**
 * @author ytjia created on 2017-09-14 14:19
 */
public class WordBreak {

  /**
   * Given a non-empty string s and a dictionary wordDict containing a list of non-empty words,
   * determine if s can be segmented into a space-separated sequence of one or more dictionary
   * words. You may assume the dictionary does not contain duplicate words.
   * <p>
   * For example, given s = "leetcode", dict = ["leet", "code"].
   * <p>
   * Return true because "leetcode" can be segmented as "leet code".
   * <p>
   * UPDATE (2017/1/4): The wordDict parameter had been changed to a list of strings (instead of a
   * set of strings). Please reload the code definition to get the latest changes.
   * <p>
   * https://leetcode.com/problems/word-break/description/
   */
  class Solution {

    public boolean wordBreak(String s, List<String> wordDict) {
      boolean[] status = new boolean[s.length() + 1];
      Set<String> wordDictSet = new HashSet<>(wordDict);
      status[0] = true;
      for (int i = 1; i < s.length() + 1; i++) {
        for (int j = 0; j < i; j++) {
          if (status[j] && wordDictSet.contains(s.substring(j, i))) {
            status[i] = true;
            break;
          }
        }
      }

      return status[s.length()];
    }
  }

}
