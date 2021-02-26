#
# @lc app=leetcode id=73 lang=python3
#
# [73] Set Matrix Zeroes
#

# @lc code=start
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        lsti, lstj = set(), set()
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    lsti.add(i)
                    lstj.add(j)
        for i in lsti:
            for k in range(n):
                matrix[i][k] = 0
        for j in lstj:
            for k in range(m):
                matrix[k][j] = 0
        return matrix
        # how to solve it using constance space?
        
# @lc code=end

