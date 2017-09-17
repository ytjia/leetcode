package leetcode;

import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;

/**
 * @author ytjia created on 2017-09-15 18:01
 */
public class FriendCircles {

  /**
   * There are N students in a class. Some of them are friends, while some are not. Their friendship
   * is transitive in nature. For example, if A is a direct friend of B, and B is a direct friend of
   * C, then A is an indirect friend of C. And we defined a friend circle is a group of students who
   * are direct or indirect friends.
   * <p>
   * Given a N*N matrix M representing the friend relationship between students in the class. If
   * M[i][j] = 1, then the ith and jth students are direct friends with each other, otherwise not.
   * And you have to output the total number of friend circles among all the students.
   * <p>
   * https://leetcode.com/problems/friend-circles/description/
   */
  class Solution {

    public int findCircleNum(int[][] M) {
      int[] visited = new int[M.length];
      int counter = 0;
      for (int i = 0; i < M.length; i++) {
        if (visited[i] == 0) {
          dfs(i, M, visited);
          counter++;
        }
      }
      return counter;
    }

    private void dfs(int i, int[][] M, int[] visited) {
      for (int j = 0; j < visited.length; j++) {
        if (visited[j] == 0 && M[i][j] == 1) {
          visited[j] = 1;
          dfs(j, M, visited);
        }
      }
    }

    public int findCircleNum2(int[][] M) {
      if (M == null || M.length == 0) {
        return 0;
      }
      int stuCnt = M.length;
      Map<Integer, Integer> stuCircleDict = new HashMap<>();
      Map<Integer, List<Integer>> circleStuDict = new HashMap<>();
      for (int i = 0; i < stuCnt; i++) {
        stuCircleDict.put(i, i);
        List<Integer> stuList = new LinkedList<>();
        stuList.add(i);
        circleStuDict.put(i, stuList);
      }
      for (int i = 0; i < stuCnt - 1; i++) {
        for (int j = i + 1; j < stuCnt; j++) {
          if (M[i][j] == 1) {
            circleMerge(i, j, stuCircleDict, circleStuDict);
          }
        }
      }
      return circleStuDict.keySet().size();
    }

    private void circleMerge(int stuA, int stuB, Map<Integer, Integer> stuCircleDict,
        Map<Integer, List<Integer>> circleStuDict) {
      if (stuCircleDict.get(stuA).equals(stuCircleDict.get(stuB))) {
        return;
      } else {
        int mergedCircle = stuCircleDict.get(stuA);
        int stuBCircle = stuCircleDict.get(stuB);
        circleStuDict.get(mergedCircle).addAll(circleStuDict.get(stuBCircle));
        for (int stu : circleStuDict.get(stuBCircle)) {
          stuCircleDict.replace(stu, mergedCircle);
        }
        circleStuDict.remove(stuBCircle);
      }
    }
  }
}
