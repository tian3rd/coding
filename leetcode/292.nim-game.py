#
# @lc app=leetcode id=292 lang=python3
#
# [292] Nim Game
#

# @lc code=start
class Solution:
    def canWinNim(self, n: int) -> bool:
        # make sure you don't get to 4
        return n%4 != 0
        
# @lc code=end

