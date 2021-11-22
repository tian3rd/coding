#
# @lc app=leetcode id=567 lang=python3
#
# [567] Permutation in String
#

# @lc code=start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        i = 0
        s1_sorted = sorted(s1)
        while i + len(s1) <= len(s2):
            if s1_sorted == sorted(s2[i:i+len(s1)]):
                return True
            i += 1
        return False
        
# @lc code=end

