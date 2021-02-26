#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        rtn = [[1]*(n+1) for _ in range(m+1)]
        for i in range(2, m+1):
            for j in range(2, n+1):
                rtn[i][j] = rtn[i-1][j]+rtn[i][j-1]
        return rtn[m][n]
        
# @lc code=end

