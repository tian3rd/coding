#
# @lc app=leetcode id=459 lang=python3
#
# [459] Repeated Substring Pattern
#

# @lc code=start
from math import sqrt
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if len(s) == 1:
            return False
        if len(set(list(s))) == 1:
            return True
        # seg mark # of segments to be examined
        for seg in range(len(s)//2, 1, -1):
            if len(s)%seg != 0:
                continue
            l = len(s)//seg
            snippet = s[:l]
            for i in range(1, seg):
                if s[i*l:i*l+l] != snippet:
                    break
                if i == seg-1:
                    return True
        return False
        
# @lc code=end

