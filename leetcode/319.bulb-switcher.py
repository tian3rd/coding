#
# @lc app=leetcode id=319 lang=python3
#
# [319] Bulb Switcher
#

# @lc code=start
from math import sqrt
class Solution:
    def bulbSwitch(self, n: int) -> int:
        if n <= 0:
            return 0
        rtn = 0
        # only n = m*m can have odd number of factors then be lit after n rounds
        for i in range(n, 0, -1):
            if int(sqrt(i)) ** 2 == i:
                rtn = int(sqrt(i))
                break
        return rtn
        
# @lc code=end

