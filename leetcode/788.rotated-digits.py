#
# @lc app=leetcode id=788 lang=python3
#
# [788] Rotated Digits
#

# @lc code=start
class Solution:
    def rotatedDigits(self, N: int) -> int:
        valid = set(['2', '5', '6', '9'])
        symetry = set(['0', '1', '8'])
        invalid = set(['0', '1', '3', '4', '7', '8'])
        rtn = 0
        for i in range(N+1):
            se = set(list(str(i)))
            if se.issubset(invalid):
                continue
            if se.difference(valid).issubset(symetry):
                rtn += 1
        return rtn

        
# @lc code=end

