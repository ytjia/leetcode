package leetcode;

import org.junit.Test;

import static org.junit.Assert.assertEquals;

/**
 * Created by ytjia on 16/1/12.
 */
public class TestEditDistance {

  @Test
  public void editDistance() {
    EditDistance editDistance = new EditDistance();
    EditDistance.Solution solution = editDistance.new Solution();

    String x = "sea";
    String y = "eat";
    String z = "e";

    assertEquals(2, solution.minDistance(x, y));
    assertEquals(2, solution.minDistance(x, z));
  }
}
