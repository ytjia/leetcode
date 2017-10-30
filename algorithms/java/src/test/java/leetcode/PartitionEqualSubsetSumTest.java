package leetcode;

import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;

/**
 * @author ytjia created on 2017-10-30 16:52
 */
public class PartitionEqualSubsetSumTest {

  PartitionEqualSubsetSum.Solution solution;

  @Before
  public void setUp() throws Exception {
    PartitionEqualSubsetSum partitionEqualSubsetSum = new PartitionEqualSubsetSum();
    solution = partitionEqualSubsetSum.new Solution();
  }

  @Test
  public void testCanPartition() throws Exception {
    int[] nums1 = new int[]{1, 5, 11, 5};
    int[] nums2 = new int[]{1, 2, 3, 5};
    Assert.assertTrue(solution.canPartition(nums1));
    Assert.assertFalse(solution.canPartition(nums2));
  }


}
