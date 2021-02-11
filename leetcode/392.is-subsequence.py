#
# @lc app=leetcode id=392 lang=python3
#
# [392] Is Subsequence
#

# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # two pointers
        if len(s) > len(t):
            return False
        if len(s) == 0:
            return True
        ps = 0
        for pt in range(len(t)):
            if s[ps] == t[pt]:
                ps += 1
            if ps >= len(s):
                return True
        return False
        
# @lc code=end

