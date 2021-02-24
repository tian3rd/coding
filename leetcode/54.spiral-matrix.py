#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#

# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rtn = []
        def outside(matrix: List[List[int]], rtn):
            # check both row and col 
            if len(matrix) == 0 or len(matrix[0]) == 0:
                return
            if len(matrix) == 1:
                rtn += matrix[0][:]
                return
            if len(matrix[0]) == 1:
                rtn += [matrix[i][0] for i in range(len(matrix))]
                return
            row, col = len(matrix), len(matrix[0])

            # first row
            rtn += matrix[0][:] 
            # last col excluding first and last row elements
            rtn += [matrix[r][col-1] for r in range(1, row-1)]
            # last row
            rtn += list(reversed(matrix[row-1][:])) 
            # first col excluding ...
            rtn += [matrix[r][0] for r in range(row-2,0,-1)]

            matrix = [r[1:col-1] for r in matrix[1:row-1]]
            outside(matrix, rtn)
        
        outside(matrix, rtn)
        return rtn
        
# @lc code=end

