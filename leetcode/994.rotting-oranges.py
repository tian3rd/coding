#
# @lc app=leetcode id=994 lang=python3
#
# [994] Rotting Oranges
#

# @lc code=start
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def is_fresh(grid):
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == 1:
                        return True
            return False
        
        if not is_fresh(grid):
            return 0
        rtn = -1
        row, col = len(grid), len(grid[0])
        q = collections.deque()
        visited = [[False for _ in range(col)] for _ in range(row)]
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    q.append((i, j))
                    visited[i][j] = True
        while q:
            sz = len(q)
            rtn += 1
            for _ in range(sz):
                x, y = q.popleft()
                for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < row and 0 <= ny < col and not visited[nx][ny] and grid[nx][ny] == 1:
                        q.append((nx, ny))
                        visited[nx][ny] = True
                        grid[nx][ny] = 2
        return rtn if not is_fresh(grid) else -1


        
# @lc code=end

