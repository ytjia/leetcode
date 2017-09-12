package leetcode;

/**
 * @author ytjia created on 2017-09-12 22:51
 */
public class BestTimetoBuyandSellStock {

  /**
   * Say you have an array for which the ith element is the price of a given stock on day i.
   * <p>
   * If you were only permitted to complete at most one transaction (ie, buy one and sell one share
   * of the stock), design an algorithm to find the maximum profit.
   * <p>
   * https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
   */
  class Solution {

    public int maxProfit(int[] prices) {
      int maxProfit = 0;
      if (prices == null || prices.length <= 1) {
        return maxProfit;
      }
      int minBuy = prices[0];
      int profit;
      for (int i = 1; i < prices.length; i++) {
        profit = prices[i] - minBuy;
        maxProfit = Math.max(maxProfit, profit);
        minBuy = Math.min(minBuy, prices[i]);
      }

      return maxProfit;
    }
  }

}
