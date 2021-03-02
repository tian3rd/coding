#
# @lc app=leetcode id=1716 lang=python3
#
# [1716] Calculate Money in Leetcode Bank
#

# @lc code=start
class Solution:
    def totalMoney(self, n: int) -> int:
        wholeweeks = n // 7
        wholeweeks_savings = (7*wholeweeks + 49) * wholeweeks // 2
        leftdays = n % 7
        if leftdays == 0:
            return wholeweeks_savings
        return leftdays * (wholeweeks * 2 + leftdays + 1) // 2 + wholeweeks_savings
        
# @lc code=end

