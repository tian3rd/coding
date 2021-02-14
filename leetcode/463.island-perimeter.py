#
# @lc app=leetcode id=463 lang=python3
#
# [463] Island Perimeter
#

# @lc code=start
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        nrows, ncols = len(grid), len(grid[0])
        lines = 0
        for row in range(nrows):
            for col in range(ncols):
                if grid[row][col] != 0:
                    if row == 0:
                        lines += 1
                        if row+1 < nrows:
                            lines += 1-grid[row+1][col]
                    if row == nrows-1:
                        lines += 1
                        if row-1 > -1:
                            lines += 1-grid[row-1][col]
                    if 0<row and row<nrows-1:
                        lines += 2-(grid[row-1][col]+grid[row+1][col])

                    if col == 0:
                        lines += 1
                        if col+1 < ncols:
                            lines += 1-grid[row][col+1]
                    if col == ncols-1:
                        lines += 1
                        if col-1 > -1:
                            lines += 1-grid[row][col-1]
                    if 0<col and col<ncols-1:
                        lines += 2-(grid[row][col-1]+grid[row][col+1])
        return lines

# @lc code=end

