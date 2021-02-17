#
# @lc app=leetcode id=693 lang=python3
#
# [693] Binary Number with Alternating Bits
#

# @lc code=start
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        rtn = n + (n>>1) + 1
        while rtn%2==0:
            rtn //= 2
        return rtn == 1
        
# @lc code=end

