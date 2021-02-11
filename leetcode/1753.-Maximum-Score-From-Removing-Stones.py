#
# @lc app=leetcode id=1753 lang=python3
#
# [1753] Maximum Score From Removing Stones
#

# @lc code=start
class Solution(object):
    def maximumScore(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        a, b, c = tuple(sorted([a, b, c]))
        return self.ms(a,b,c)
    
    def ms(self, a, b, c):
        if a+b <= c:
            return a+b
        return self.ms(a-1, b-1, c)+1