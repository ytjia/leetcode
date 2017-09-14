package leetcode;

/**
 * @author ytjia created on 2017-09-13 18:10
 */
public class LongestPalindromicSubstring {

  /**
   * Given a string s, find the longest palindromic substring in s. You may assume that the maximum
   * length of s is 1000.
   * <p>
   * https://leetcode.com/problems/longest-palindromic-substring/description/
   */
  class Solution {

    /**
     * TimeCost = On
     */
    public String longestPalindrome(String s) {
      String optS = preProcess(s);
      int optSLens = optS.length();

      int[] lensArr = new int[optSLens];
      lensArr[0] = 0;
      int centerIndex = 0;
      int rightBorder = 0;
      for (int i = 1; i < optSLens - 1; i++) {
        int mirrorI = centerIndex * 2 - i;
        if (i < rightBorder) {
          lensArr[i] = Math.min(lensArr[mirrorI], rightBorder - i);
        } else {
          lensArr[i] = 0;
        }

        while (optS.charAt(i + lensArr[i] + 1) == optS.charAt(i - lensArr[i] - 1)) {
          lensArr[i]++;
        }

        if (i + lensArr[i] > rightBorder) {
          centerIndex = i;
          rightBorder = i + lensArr[i];
        }
      }

      int maxLength = 0;
      int maxCenter = 0;
      for (int i = 1; i < optSLens - 1; i++) {
        if (lensArr[i] > maxLength) {
          maxLength = lensArr[i];
          maxCenter = i;
        }
      }

      return s.substring((maxCenter - 1 - maxLength) / 2, (maxCenter - 1 + maxLength) / 2);
    }

    /**
     * "abcb" -> "^#a#b#c#b#$"
     */
    private String preProcess(String s) {
      int lens = s.length();
      if (lens == 0) {
        return "^$";
      }
      StringBuilder sb = new StringBuilder();
      sb.append("^#");
      for (int i = 0; i < lens; i++) {
        sb.append(s.charAt(i));
        sb.append("#");
      }
      sb.append("$");
      return sb.toString();
    }

    public String longestPalindromeOn2(String s) {
      int begin = 0;
      int end = 0;
      for (int i = 0; i < s.length(); i++) {
        int l1 = extendCenter(s, i, i);
        int l2 = extendCenter(s, i, i + 1);
        int l = Math.max(l1, l2);
        if (l > end - begin) {
          begin = i - (l - 1) / 2;
          end = i + l / 2 + 1;
        }
      }
      return s.substring(begin, end);
    }

    private int extendCenter(String s, int left, int right) {
      while (left >= 0 && right < s.length() && s.charAt(left) == s.charAt(right)) {
        left--;
        right++;
      }

      return right - left - 1;
    }
  }

}
