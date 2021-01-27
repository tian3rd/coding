#
# @lc app=leetcode id=6 lang=python3
#
# [6] ZigZag Conversion
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        period = 2*numRows - 2
        cycles = len(s)//period + 1
        lines = {key: "" for key in range(numRows)}
        for i in range(cycles):
            for j in range(period//2):
                if period*i+j < len(s):
                    lines[j] += s[period*i+j]
            for k in range(period//2, period):
                if period*i+k < len(s):
                    lines[period-k] += s[period*i+k]
        rtn = ""
        for i in range(numRows):
            rtn += lines[i]
        return rtn

        
# @lc code=end

