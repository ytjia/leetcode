package leetcode;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;

/**
 * @author ytjia created on 2017-09-15 20:06
 */
public class CombinationSum {


  /**
   * Given a set of candidate numbers (C) (without duplicates) and a target number (T), find all
   * unique combinations in C where the candidate numbers sums to T.
   * <p>
   * The same repeated number may be chosen from C unlimited number of times.
   * <p>
   * https://leetcode.com/problems/combination-sum/description/
   */
  class Solution {

    public List<List<Integer>> combinationSum(int[] candidates, int target) {
      List<List<Integer>> combination = new LinkedList<>();
      Arrays.sort(candidates);
      backTrack(combination, new ArrayList<>(), candidates, target, 0);
      return combination;
    }

    private void backTrack(List<List<Integer>> combination, List<Integer> tmpList, int[] candidates,
        int target, int start) {
      if (target < 0) {
        return;
      } else if (target == 0) {
        combination.add(new ArrayList<>(tmpList));
      } else {
        for (int i = start; i < candidates.length; i++) {
          tmpList.add(candidates[i]);
          backTrack(combination, tmpList, candidates, target - candidates[i], i);
          tmpList.remove(tmpList.size() - 1);
        }
      }
    }
  }

}
