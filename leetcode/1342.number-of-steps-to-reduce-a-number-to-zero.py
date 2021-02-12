#
# @lc app=leetcode id=1342 lang=python3
#
# [1342] Number of Steps to Reduce a Number to Zero
#

# @lc code=start
class Solution:
    def numberOfSteps (self, num: int) -> int:
        rtn = 0
        while num != 0:
            num = num/2 if num%2 == 0 else num-1
            rtn += 1
        return rtn
        
# @lc code=end

