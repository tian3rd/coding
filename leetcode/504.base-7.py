#
# @lc app=leetcode id=504 lang=python3
#
# [504] Base 7
#

# @lc code=start
class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        sign = -1 if num<0 else 1
        num *= sign
        rtn = ""
        while num != 0:
            rtn += (str(num%7))
            num //= 7
        return "-"+rtn[::-1] if sign==-1 else rtn[::-1]

        
# @lc code=end

