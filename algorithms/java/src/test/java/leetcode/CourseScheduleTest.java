package leetcode;

import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;

/**
 * @author ytjia created on 2017-09-21 17:56
 */
public class CourseScheduleTest {

  CourseSchedule.Solution solution;

  @Before
  public void setUp() throws Exception {
    CourseSchedule courseSchedule = new CourseSchedule();
    solution = courseSchedule.new Solution();
  }

  @Test
  public void testCanFinish() throws Exception {
    int[][] pre = {{0, 1}, {1, 3}, {3, 1}, {3, 2}};
    Assert.assertFalse(solution.canFinish(4, pre));
  }

}
