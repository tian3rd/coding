#
# @lc app=leetcode id=63 lang=python3
#
# [63] Unique Paths II
#

# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        rtn = [[1]*(n+1) for _ in range(m+1)]
        for m0 in range(m):
            for n0 in range(n):
                if obstacleGrid[m0][n0] == 1:
                    rtn[m-m0][n-n0] = 0
                    if m0 == m-1:
                        rtn[(n-n0):][1] = 0
                    if n0 == n-1:
                        # rtn[1][(m-m0):] = 0
                        for k in range(m-m0, m+1):
                            rtn[1][k] = 0
        if m == 1 or n == 1:
            return rtn[m][n]
        for i in range(2, m+1):
            for j in range(2, n+1):
                if rtn[i][j] != 0:
                    rtn[i][j] = rtn[i][j-1]+rtn[i-1][j]
        return rtn[m][n]
        
# @lc code=end

