package leetcode;

/**
 * @author ytjia created on 2017-09-20 18:06
 */
public class NumberofIslands {

  /**
   * Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is
   * surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You
   * may assume all four edges of the grid are all surrounded by water.
   * <p>
   * https://leetcode.com/problems/number-of-islands/description/
   */
  class Solution {

    // dfs
    public int numIslands(char[][] grid) {
      if (grid == null || grid.length == 0 || grid[0].length == 0) {
        return 0;
      }
      int[][] visited = new int[grid.length][grid[0].length];
      int counter = 0;
      for (int i = 0; i < grid.length; i++) {
        for (int j = 0; j < grid[i].length; j++) {
          if (grid[i][j] == '1' && visited[i][j] == 0) {
            counter++;
            dfs(grid, visited, i, j);
          }
        }
      }
      return counter;
    }

    private void dfs(char[][] grid, int[][] visited, int i, int j) {
      if (i < 0 || i >= grid.length || j < 0 || j >= grid[0].length || visited[i][j] == 1) {
        return;
      }
      visited[i][j] = 1;
      if (grid[i][j] == '0') {
        return;
      }
      dfs(grid, visited, i - 1, j);
      dfs(grid, visited, i + 1, j);
      dfs(grid, visited, i, j - 1);
      dfs(grid, visited, i, j + 1);
    }
  }

}
