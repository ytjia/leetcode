package leetcode;

import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;

import java.util.ArrayList;
import java.util.List;

/**
 * @author ytjia created on 2017-09-11 17:31
 */
public class SubsetsTest {

  Subsets.Solution solution;

  @Before
  public void setUp() throws Exception {
    Subsets subsets = new Subsets();
    solution = subsets.new Solution();
  }

  @Test
  public void testSubsets() throws Exception {
    int[] nums = new int[3];
    nums[0] = 1;
    nums[1] = 2;
    nums[2] = 3;

    System.out.println(solution.subsets(nums));

  }

}
