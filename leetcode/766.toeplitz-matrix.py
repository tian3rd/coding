#
# @lc app=leetcode id=766 lang=python3
#
# [766] Toeplitz Matrix
#

# @lc code=start
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        row, col = len(matrix), len(matrix[0])
        if row == 1 or col == 1:
            return True
        for i in range(row-1):
            for j in range(col-1):
                if matrix[i][j] != matrix[i+1][j+1]:
                    return False
        return True
        
# @lc code=end

