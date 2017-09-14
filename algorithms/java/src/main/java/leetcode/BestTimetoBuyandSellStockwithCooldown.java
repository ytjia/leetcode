package leetcode;

/**
 * @author ytjia created on 2017-09-13 12:38
 */
public class BestTimetoBuyandSellStockwithCooldown {

  /**
   * Say you have an array for which the ith element is the price of a given stock on day i.
   * <p>
   * Design an algorithm to find the maximum profit. You may complete as many transactions as you
   * like (ie, buy one and sell one share of the stock multiple times) with the following
   * restrictions:
   * <p>
   * You may not engage in multiple transactions at the same time (ie, you must sell the stock
   * before you buy again). After you sell your stock, you cannot buy stock on next day. (ie,
   * cooldown 1 day)
   * <p>
   * https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/description/
   */
  class Solution {

    public int maxProfit(int[] prices) {
      if (prices == null) {
        return 0;
      }
      int pre_sell = 0;
      int sell = 0;
      int pre_buy;
      int buy = Integer.MIN_VALUE;
      for (int price : prices) {
        pre_buy = buy;
        buy = Math.max(pre_sell - price, pre_buy);
        pre_sell = sell;
        sell = Math.max(pre_buy + price, pre_sell);
      }
      return sell;
    }
  }
}
