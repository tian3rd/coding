#
# @lc app=leetcode id=441 lang=python3
#
# [441] Arranging Coins
#

# @lc code=start
from math import sqrt
class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n == 0:
            return 0
        rtn = int(sqrt(2*n))-1
        while int((1+rtn)*rtn/2) <= n:
            if int((rtn+1)*(rtn+2)/2) > n:
                return rtn
            rtn += 1
        
# @lc code=end

