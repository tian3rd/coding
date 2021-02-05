#
# @lc app=leetcode id=171 lang=python3
#
# [171] Excel Sheet Column Number
#

# @lc code=start
import string
class Solution:
    def titleToNumber(self, s: str) -> int:
        nums = [_ for _ in range(1, 27)]
        letters = string.ascii_uppercase
        dic = dict(zip(letters, nums))
        rtn = 0
        for i in range(len(s)):
            rtn = 26*rtn + dic[s[i]]
        return rtn
        
# @lc code=end

