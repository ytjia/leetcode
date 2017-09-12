package leetcode;

/**
 * @author ytjia created on 2017-09-12 17:10
 */
public class PalindromicSubstrings {


  /**
   * Given a string, your task is to count how many palindromic substrings in this string.
   * <p>
   * The substrings with different start indexes or end indexes are counted as different substrings
   * even they consist of same characters.
   * <p>
   * https://leetcode.com/problems/palindromic-substrings/description/
   */
  class Solution {

    int count = 0;

    public int countSubstrings(String s) {
      if (s == null) {
        return count;
      }
      for (int i = 0; i < s.length(); i++) {
        statPalindromic(s, i, i);
        statPalindromic(s, i, i + 1);
      }

      return count;
    }

    public void statPalindromic(String s, int start, int end) {
      while (start >= 0 && end < s.length() && s.charAt(start) == s.charAt(end)) {
        count++;
        start--;
        end++;
      }
    }
  }

}
