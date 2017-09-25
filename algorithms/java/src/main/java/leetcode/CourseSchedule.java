package leetcode;

import java.util.HashMap;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.Set;

/**
 * @author ytjia created on 2017-09-21 17:23
 */
public class CourseSchedule {

  /**
   * There are a total of n courses you have to take, labeled from 0 to n - 1.
   * <p>
   * Some courses may have prerequisites, for example to take course 0 you have to first take course
   * 1, which is expressed as a pair: [0,1]
   * <p>
   * Given the total number of courses and a list of prerequisite pairs, is it possible for you to
   * finish all courses?
   * <p>
   * https://leetcode.com/problems/course-schedule/description/
   */
  class Solution {

    public boolean canFinish(int numCourses, int[][] prerequisites) {
      if (numCourses <= 0 || prerequisites == null || prerequisites.length == 0) {
        return true;
      }
      Map<Integer, List<Integer>> prerequisitesMap = new HashMap<>();
      for (int[] prerequisite : prerequisites) {
        prerequisitesMap.putIfAbsent(prerequisite[0], new LinkedList<Integer>());
        prerequisitesMap.get(prerequisite[0]).add(prerequisite[1]);
      }
      int[] visited = new int[numCourses];
      for (int i = 0; i < numCourses; i++) {
        if (visited[i] == 0) {
          if (hasCircle(visited, prerequisitesMap, i, new HashSet<>())) {
            return false;
          }
        }
      }
      return true;
    }

    private boolean hasCircle(int[] visited, Map<Integer, List<Integer>> prerequisitesMap,
        int target, Set<Integer> path) {
      visited[target] = 1;
      path.add(target);
      if (prerequisitesMap.containsKey(target)) {
        for (int next : prerequisitesMap.get(target)) {
          if (path.contains(next)) {
            return true;
          } else if (visited[next] == 1) {
            continue;
          } else {
            visited[next] = 1;
            path.add(next);
            if (hasCircle(visited, prerequisitesMap, next, path)) {
              return true;
            }
            path.remove(next);
          }
        }
      }
      return false;
    }
  }

}
