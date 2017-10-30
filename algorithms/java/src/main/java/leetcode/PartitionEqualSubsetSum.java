package leetcode;

/**
 * @author ytjia created on 2017-10-30 16:33
 */
public class PartitionEqualSubsetSum {

  /**
   * Given a non-empty array containing only positive integers, find if the array can be partitioned
   * into two subsets such that the sum of elements in both subsets is equal.
   * <p>
   * https://leetcode.com/problems/partition-equal-subset-sum/description/
   */
  class Solution {

    private int NUM_MAX = 100;

    public boolean canPartition(int[] nums) {
      int[] statArr = new int[NUM_MAX + 1];
      int sum = 0;
      for (int num : nums) {
        ++statArr[num];
        sum += num;
      }
      if (sum % 2 == 0) {
        return existSubsetEqualSum(statArr, sum / 2);
      } else {
        return false;
      }
    }

    private boolean existSubsetEqualSum(int[] statArr, int targetSum) {
      int beginIndex = Math.min(NUM_MAX, targetSum);
      for (int i = beginIndex; i >= 0; --i) {
        if (statArr[i] > 0) {
          int restSum = targetSum - i;
          if (restSum == 0) {
            return true;
          } else if (restSum > 0) {
            --statArr[i];
            boolean result = existSubsetEqualSum(statArr, restSum);
            if (result) {
              return result;
            }
            ++statArr[i];
          }
        }
      }
      return false;
    }
  }

}
