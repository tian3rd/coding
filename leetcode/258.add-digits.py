#
# @lc app=leetcode id=258 lang=python3
#
# [258] Add Digits
#

# @lc code=start
class Solution:
    def addDigits(self, num: int) -> int:
        # no loop/recursion in O(1) time?
        # just find the pattern...
        if num < 10 and num >=0:
            return num
        if num%9 == 0:
            return 9
        return num%9
        
# @lc code=end

