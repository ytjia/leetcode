package leetcode;

import java.util.ArrayList;
import java.util.List;
import java.util.HashSet;
import java.util.Set;

/**
 * Accepted
 * https://leetcode.com/problems/gray-code/
 * Created by ytjia on 15/8/14.
 */
public class GrayCode {

  public class Solution {

    Integer changeBit(Integer target, Integer position) {
      int t = (int)Math.pow(2, position);
      if ((target & t) > 0) {
        return target - t;
      } else {
        return target + t;
      }
    }

    public List<Integer> grayCode(int n) {
      Set<Integer> set = new HashSet<Integer>();
      List<Integer> list = new ArrayList<Integer>();

      for (int i = 0; i < Math.pow(2, n); i++) {
        set.add(i);
      }
      int cur = 0;
      while (!set.isEmpty()) {
        list.add(cur);
        set.remove(cur);
        for (int j = 0; j < n; j++) {
          int gray = changeBit(cur, j);
          if (set.contains(gray)) {
            cur = gray;
            break;
          }
        }
      }

      return list;
    }

    public List<Integer> grayCode2(int n) {
      List<Integer> list = new ArrayList<Integer>();

      if (n < 0) {
        return list;
      }
      if (n == 0) {
        list.add(0);
        return list;
      }
      list.add(0);
      list.add(1);
      for (int i = 2; i <= n; i++) {
        for (int j = list.size() - 1; j >= 0; j--) {
          list.add(list.get(j) + (1 << (i - 1)));
        }
      }

      return list;
    }
  }
}
