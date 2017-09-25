package leetcode;

/**
 * @author ytjia created on 2017-09-21 14:39
 */
public class ArrayNesting {

  /**
   * A zero-indexed array A consisting of N different integers is given. The array contains all
   * integers in the range [0, N - 1]. Sets S[K] for 0 <= K < N are defined as follows: S[K] = {
   * A[K], A[A[K]], A[A[A[K]]], ... }. Sets S[K] are finite for each K and should NOT contain
   * duplicates.
   * <p>
   * Write a function that given an array A consisting of N integers, return the size of the largest
   * set S[K] for this array.
   * <p>
   * https://leetcode.com/problems/array-nesting/description/
   */
  class Solution {

    public int arrayNesting(int[] nums) {
      if (nums == null || nums.length == 0) {
        return 0;
      }
      int numsLens = nums.length;
      int maxSetSize = 0;
      int curSetSize;
      int[] visited = new int[numsLens];
      for (int i = 0; i < numsLens; i++) {
        if (visited[i] == 0) {
          curSetSize = 0;
          int next = i;
          while (visited[next] == 0) {
            visited[next] = 1;
            next = nums[next];
            curSetSize++;
          }
          maxSetSize = Math.max(maxSetSize, curSetSize);
        }
      }

      return maxSetSize;
    }

  }
}
