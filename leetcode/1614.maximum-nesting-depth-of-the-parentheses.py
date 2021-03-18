#
# @lc app=leetcode id=1614 lang=python3
#
# [1614] Maximum Nesting Depth of the Parentheses
#

# @lc code=start
class Solution:
    def maxDepth(self, s: str) -> int:
        if s == "()":
            return 1
        if len(s) <= 3:
            return 0
        maxi, rtn = 0, 0
        for ele in s:
            if ele == '(':
                maxi += 1
                rtn = max(maxi, rtn)
            elif ele == ')':
                maxi -= 1
        return rtn

        
# @lc code=end

