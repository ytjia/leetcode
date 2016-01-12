package leetcode;

/**
 * Accepted!
 * https://leetcode.com/problems/edit-distance/
 * Created by ytjia on 16/1/12.
 */
public class EditDistance {

  public class Solution {

    public int minDistance(String word1, String word2) {
      if (word1 == null || word2 == null) {
        return -1;
      }
      int lenW1 = word1.length();
      int lenW2 = word2.length();

      int[][] arr = new int[lenW1+1][lenW2+1];
      arr[0][0] = 0;
      for (int i = 1; i <= lenW1; i++) {
        arr[i][0] = i;
      }
      for (int i = 1; i <= lenW2; i++) {
        arr[0][i] = i;
      }
      for (int i = 1; i <= lenW1; i++) {
        for (int j = 1; j <= lenW2; j++) {
          if (word1.charAt(i-1) == word2.charAt(j-1)) {
            arr[i][j] = arr[i-1][j-1];
          } else {
            arr[i][j] = Math.min(Math.min(arr[i][j-1], arr[i-1][j]), arr[i-1][j-1]) + 1;
          }
        }
      }

      return arr[lenW1][lenW2];
    }
  }

}
