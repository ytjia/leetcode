package leetcode;

import java.util.Arrays;
import java.util.Comparator;
import java.util.LinkedList;
import java.util.List;

/**
 * @author ytjia created on 2017-09-18 09:51
 */
public class QueueReconstructionbyHeight {

  /**
   * Suppose you have a random list of people standing in a queue. Each person is described by a
   * pair of integers (h, k), where h is the height of the person and k is the number of people in
   * front of this person who have a height greater than or equal to h. Write an algorithm to
   * reconstruct the queue.
   * <p>
   * https://leetcode.com/problems/queue-reconstruction-by-height/description/
   */
  class Solution {

    public int[][] reconstructQueue(int[][] people) {
      if (people == null || people.length == 0 || people[0].length == 0) {
        return new int[0][0];
      }

      Arrays.sort(people, new Comparator<int[]>() {
        @Override
        public int compare(int[] o1, int[] o2) {
          if (o1[0] == o2[0]) {
            return o1[1] - o2[1];
          } else {
            return o2[0] - o1[0];
          }
        }
      });

      List<int[]> queueList = new LinkedList<>();
      for (int i = 0; i < people.length; i++) {
        queueList.add(people[i][1], people[i]);
      }

      int[][] queue = new int[people.length][2];
      return queueList.toArray(queue);
    }
  }

}
