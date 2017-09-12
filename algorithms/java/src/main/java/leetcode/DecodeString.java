package leetcode;

import java.util.Collections;

/**
 * @author ytjia created on 2017-09-12 14:43
 */
public class DecodeString {

  /**
   * Given an encoded string, return it's decoded string.
   * <p>
   * The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is
   * being repeated exactly k times. Note that k is guaranteed to be a positive integer.
   * <p>
   * You may assume that the input string is always valid; No extra white spaces, square brackets
   * are well-formed, etc.
   * <p>
   * Furthermore, you may assume that the original data does not contain any digits and that digits
   * are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].
   * <p>
   * https://leetcode.com/problems/decode-string/description/
   */
  class Solution {

    public String decodeString(String s) {
      StringBuilder sb = new StringBuilder();
      StringBuilder tSb = new StringBuilder();

      // 0: no coding, 1: in square brackets
      int status = 0;
      int times = 0;
      int brackets = 0;
      for (char c : s.toCharArray()) {
        switch (status) {
          case 0: {
            if (c >= '0' && c <= '9') {
              times = times * 10 + Character.getNumericValue(c);
            } else if (c == '[') {
              tSb = new StringBuilder();
              brackets = 1;
              status = 1;
            } else {
              sb.append(c);
            }
            break;
          }
          case 1: {
            if (c == ']') {
              brackets -= 1;
              if (brackets == 0) {
                sb.append(
                    String.join("", Collections.nCopies(times, decodeString(tSb.toString()))));
                times = 0;
                status = 0;
                break;
              }
            } else {
              if (c == '[') {
                brackets += 1;
              }
            }
            tSb.append(c);
            break;
          }
        }

      }
      return sb.toString();
    }
  }

}
