package leetcode;

import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;

/**
 * @author ytjia created on 2017-09-20 19:37
 */
public class MedianofTwoSortedArraysTest {

  MedianofTwoSortedArrays.Solution solution;

  @Before
  public void setUp() throws Exception {
    MedianofTwoSortedArrays medianofTwoSortedArrays = new MedianofTwoSortedArrays();
    solution = medianofTwoSortedArrays.new Solution();
  }

  @Test
  public void testFindMedianSortedArrays() throws Exception {
    int[] nums1 = new int[]{1, 3};
    int[] nums2 = new int[]{2};
    int[] nums3 = new int[]{1, 1, 3, 3};
    int[] nums4 = new int[]{1, 2};
    int[] nums5 = new int[]{3, 4};
    Assert.assertEquals(2.0, solution.findMedianSortedArrays(nums1, nums2), 0.000001);
    Assert.assertEquals(2.0, solution.findMedianSortedArrays(nums3, nums3), 0.000001);
    Assert.assertEquals(2.5, solution.findMedianSortedArrays(nums4, nums5), 0.000001);
  }

}
