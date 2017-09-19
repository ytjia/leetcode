package leetcode;

import java.util.ArrayList;
import java.util.List;

/**
 * @author ytjia created on 2017-09-19 14:24
 */
public class GenerateParentheses {

  /**
   * Given n pairs of parentheses, write a function to generate all combinations of well-formed
   * parentheses.
   * <p>
   * https://leetcode.com/problems/generate-parentheses/description/
   */
  class Solution {

    public List<String> generateParenthesis(int n) {
      if (n <= 0) {
        return new ArrayList<String>(0);
      }

      List<String> parenthesisList = new ArrayList<>();
      int leftCnt = n;
      int rightCnt = 0;
      generateParenthesis(leftCnt, rightCnt, parenthesisList, new StringBuilder());
      return parenthesisList;
    }

    private void generateParenthesis(int left, int right, List<String> res, StringBuilder sb) {
      if (left == 0 && right == 0) {
        res.add(sb.toString());
      } else {
        if (left > 0) {
          generateParenthesis(left - 1, right + 1, res, sb.append("("));
          sb.deleteCharAt(sb.length() - 1);
        }
        if (right > 0) {
          generateParenthesis(left, right - 1, res, sb.append(")"));
          sb.deleteCharAt(sb.length() - 1);
        }
      }
    }
  }

}
