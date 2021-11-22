#
# @lc app=leetcode id=695 lang=python3
#
# [695] Max Area of Island
#

# @lc code=start
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        width, height = len(grid[0]), len(grid)
        visited = [[False for _ in range(width)] for _ in range(height)]
        rtn = 0
        for i in range(height):
            for j in range(width):
                if grid[i][j] == 1 and not visited[i][j]:
                    # treat q as a queue
                    q = []
                    q.append([i, j])
                    visited[i][j] = True
                    area = 1
                    while q:
                        sz = len(q)
                        for _ in range(sz):
                            x, y = q.pop(0)
                            # up, down, right, left
                            for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                                nx, ny = x + dx, y + dy
                                # within grid, not visited, and has value
                                if 0 <= nx < height and 0 <= ny < width and not visited[nx][ny] and grid[nx][ny] == 1:
                                    q.append([nx, ny])
                                    visited[nx][ny] = True
                                    area += 1
                    rtn = max(rtn, area)
        return rtn


        
# @lc code=end

