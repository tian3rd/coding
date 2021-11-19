#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#

# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1 for _ in range(amount+1)]
        dp[0] = 0
        for j in range(0, amount):
            mini = amount + 1
            for i in range(len(coins)):
                if j + 1 >= coins[i] and dp[j + 1 - coins[i]] != -1:
                    mini = min(mini, dp[j + 1 - coins[i]] + 1)
            dp[j + 1] = mini if mini != amount + 1 else -1
        return dp[amount]

        
# @lc code=end

