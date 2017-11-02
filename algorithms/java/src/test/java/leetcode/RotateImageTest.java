package leetcode;

import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;

/**
 * @author ytjia created on 2017-10-31 19:26
 */
public class RotateImageTest {

  RotateImage.Solution solution;

  @Before
  public void setUp() throws Exception {
    RotateImage rotateImage = new RotateImage();
    solution = rotateImage.new Solution();
  }

  @Test
  public void testRotate() throws Exception {
    int[] a1 = new int[]{5, 1, 9, 11};
    int[] a2 = new int[]{2, 4, 8, 10};
    int[] a3 = new int[]{13, 3, 6, 7};
    int[] a4 = new int[]{15, 14, 12, 16};

    int[][] arr2d = new int[][]{a1, a2, a3, a4};

    solution.rotate(arr2d);
    System.out.println(arr2d);
  }

}
