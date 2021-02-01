#
# @lc app=leetcode id=122 lang=python3
#
# [122] Best Time to Buy and Sell Stock II
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = 0, 0
        profit, trade = 0, 0
        
        for i in range(1, len(prices)):
            sell = i
            # if prices[sell] <= prices[buy]:
            #     profit += trade
            #     trade = 0
            #     buy = i
            # else:
            #     if trade < prices[sell] - prices[buy]:
            #         trade = prices[sell] - prices[buy]
            #     else:
            #         profit += trade
            #         buy = i
            #         trade = 0
            if trade < prices[sell] - prices[buy]:
                trade = prices[sell] - prices[buy]
            else:
                profit += trade
                buy = i
                trade = 0
        if trade > 0:
            profit += trade
            trade = 0
        
        return profit
        
# @lc code=end

