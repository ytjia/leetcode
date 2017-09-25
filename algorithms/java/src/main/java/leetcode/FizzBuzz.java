package leetcode;

import java.util.ArrayList;
import java.util.List;

/**
 * @author ytjia created on 2017-09-21 20:14
 */
public class FizzBuzz {

  /**
   * Write a program that outputs the string representation of numbers from 1 to n.
   * <p>
   * But for multiples of three it should output “Fizz” instead of the number and for the multiples
   * of five output “Buzz”. For numbers which are multiples of both three and five output
   * “FizzBuzz”.
   * <p>
   * https://leetcode.com/problems/fizz-buzz/description/
   */
  class Solution {

    public List<String> fizzBuzz(int n) {
      List<String> res = new ArrayList<>();
      for (int i = 1; i <= n; i++) {
        res.add(Integer.toString(i));
      }

      for (int i = 3; i <= n; i += 3) {
        res.set(i - 1, "Fizz");
      }

      for (int i = 5; i <= n; i += 5) {
        if (res.get(i - 1).equals("Fizz")) {
          res.set(i - 1, "FizzBuzz");
        } else {
          res.set(i - 1, "Buzz");
        }
      }

      return res;
    }
  }

}
