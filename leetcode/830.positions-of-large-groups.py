#
# @lc app=leetcode id=830 lang=python3
#
# [830] Positions of Large Groups
#

# @lc code=start
class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        if len(s)<3:
            return[]
        rtn = []
        i = 0
        while i < len(s)-1:
            l = 1
            while i+l < len(s) and s[i] == s[i+l]:
                l += 1
            if l > 2:
                rtn.append([i, i+l-1])
            i += l
        return rtn
        
# @lc code=end

