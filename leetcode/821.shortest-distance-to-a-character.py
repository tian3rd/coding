#
# @lc app=leetcode id=821 lang=python3
#
# [821] Shortest Distance to a Character
#

# @lc code=start
class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        clst = [i for i in range(len(s)) if s[i]==c]
        clst = [-clst[0]] + clst + [clst[-1]]
        cindex = 1
        rtn = []
        for i in range(len(s)):
            if s[i] == c:
                rtn.append(0)
                cindex += 1
            else:
                rtn.append(min(abs(clst[cindex]-i), abs(clst[cindex-1]-i)))
        return rtn
        
# @lc code=end

