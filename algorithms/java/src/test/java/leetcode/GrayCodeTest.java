package leetcode;

import org.junit.Test;

import java.util.ArrayList;

import static org.junit.Assert.assertEquals;

/**
 * Created by ytjia on 15/8/14.
 */
public class GrayCodeTest {

  @Test
  public void grayCode() {
    GrayCode f = new GrayCode();
    GrayCode.Solution s = f.new Solution();

    ArrayList<Integer> t1 = new ArrayList<Integer>();
    t1.add(0);
    t1.add(1);
    t1.add(3);
    t1.add(2);
    assertEquals(t1, s.grayCode2(2));
  }

}
