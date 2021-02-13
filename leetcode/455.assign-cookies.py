#
# @lc app=leetcode id=455 lang=python3
#
# [455] Assign Cookies
#

# @lc code=start
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        satisfied = 0
        g = sorted(g)
        s = sorted(s)
        # two pointers of g and s
        pg, ps = 0, 0
        while pg != len(g) and ps != len(s):
            if g[pg] <= s[ps]:
                pg += 1
                satisfied += 1
            ps += 1
        return satisfied
        
# @lc code=end

