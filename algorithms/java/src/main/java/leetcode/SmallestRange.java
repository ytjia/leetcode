package leetcode;

import java.util.List;
import java.util.PriorityQueue;

/**
 * @author ytjia created on 2017-09-10 17:07
 */
public class SmallestRange {

  /**
   * You have k lists of sorted integers in ascending order. Find the smallest range that includes
   * at least one number from each of the k lists.
   * <p>
   * We define the range [a,b] is smaller than range [c,d] if b-a < d-c or a < c if b-a == d-c.
   * <p>
   * https://leetcode.com/problems/smallest-range/description/
   */
  class Solution {

    public int[] smallestRange(List<List<Integer>> nums) {
      int[] pointers = new int[nums.size()];
      int curMaxNum = Integer.MIN_VALUE;
      int minNum = 0;
      int maxNum = Integer.MAX_VALUE;
      PriorityQueue<Integer> minPointerQueue = new PriorityQueue<>(
          (a, b) -> nums.get(a).get(pointers[a]).compareTo(nums.get(b).get(pointers[b])));
      Boolean anyNumsExhausted = false;

      for (int i = 0; i < nums.size(); i++) {
        minPointerQueue.add(i);
        pointers[i] = 0;
        curMaxNum = Math.max(curMaxNum, nums.get(i).get(0));
      }
      while (!anyNumsExhausted) {
        int curMinNumsInd = minPointerQueue.poll();
        if (curMaxNum - nums.get(curMinNumsInd).get(pointers[curMinNumsInd]) < maxNum - minNum) {
          minNum = nums.get(curMinNumsInd).get(pointers[curMinNumsInd]);
          maxNum = curMaxNum;
        }
        pointers[curMinNumsInd]++;
        if (pointers[curMinNumsInd] == nums.get(curMinNumsInd).size()) {
          anyNumsExhausted = true;
        } else {
          minPointerQueue.add(curMinNumsInd);
          curMaxNum = Math.max(curMaxNum, nums.get(curMinNumsInd).get(pointers[curMinNumsInd]));
        }

      }

      return new int[]{minNum, maxNum};
    }
  }

}
