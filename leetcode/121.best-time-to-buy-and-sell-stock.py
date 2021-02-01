#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        start, end = 0, 0
        max_profit = 0
        for i in range(len(prices)):
            end = i
            if prices[end]-prices[start] < 0:
                # this is the key step: before we move start to the next smallest, we have already calculated all the possible profits and got the max profit for range 0 to i.
                start = i
            if prices[end] - prices[start] > max_profit:
                max_profit = prices[end] - prices[start]
        return max_profit

# @lc code=end

