#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0: return ""
        if len(strs) == 1: return strs[0]
        strs = sorted(strs)
        rtn = ""
        for i in range(min(len(strs[0]), len(strs[len(strs)-1]))):
            if strs[0][i] == strs[len(strs)-1][i]:
                rtn += strs[0][i]
            else: break
        return rtn

# @lc code=end

