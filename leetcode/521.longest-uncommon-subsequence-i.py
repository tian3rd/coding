#
# @lc app=leetcode id=521 lang=python3
#
# [521] Longest Uncommon Subsequence I
#

# @lc code=start
class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        if len(a) > len(b):
            return len(a)
        elif len(a) < len(b):
            return len(b)
        if a == b:
            return -1
        else:
            return len(a)
        
        
# @lc code=end

