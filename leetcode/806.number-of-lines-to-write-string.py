#
# @lc app=leetcode id=806 lang=python3
#
# [806] Number of Lines To Write String
#

# @lc code=start
class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        n = 1
        le = 0
        while True:
            linelen = 0
            while le <= len(s)-1 and linelen <= 100:
                linelen += widths[ord(s[le])-ord('a')]
                le += 1
            if le == len(s):
                return [n, linelen] if linelen<=100 else [n+1, widths[ord(s[le-1])-ord('a')]]
            if linelen > 100:
                n += 1
                le -= 1

                
            
        
# @lc code=end

