package leetcode;

import java.util.ArrayList;
import java.util.List;

/**
 * @author ytjia created on 2017-09-25 17:53
 */
public class LongestAbsoluteFilePath {

  /**
   * https://leetcode.com/problems/longest-absolute-file-path/description/
   */
  class Solution {

    public int lengthLongestPath(String input) {
      if (null == input || input.length() == 0) {
        return 0;
      }

      List<Integer> pathLengths = new ArrayList<>();
      pathLengths.add(0);
      int maxLength = 0;

      String[] dirOrFiles = input.split("\\n");
      for (String dirOrFile : dirOrFiles) {
        String[] curStrs = dirOrFile.split("\\t");
        int curLevel = curStrs.length;
        String curDirOrFile = curStrs[curLevel - 1];
        if (isFile(curDirOrFile)) {
          maxLength = Math.max(maxLength, pathLengths.get(curLevel - 1) + curDirOrFile.length());
        } else {
          pathLengths.add(curLevel, pathLengths.get(curLevel - 1) + curDirOrFile.length() + 1);
        }
      }

      return maxLength;
    }

    private boolean isFile(String dirOrFile) {
      return dirOrFile.contains(".");
    }
  }

}
