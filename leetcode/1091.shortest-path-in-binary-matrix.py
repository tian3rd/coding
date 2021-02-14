#
# @lc app=leetcode id=1091 lang=python3
#
# [1091] Shortest Path in Binary Matrix
#

# @lc code=start
from collections import deque
from typing import List
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        return self.bfs(grid)

    def bfs(self, grid: List[List[int]]) -> int:
        # set up a flag to indicate whether it's traversed: -1 is not traversed
        flag = -1
        N = len(grid)
        # start point and game point
        sx, sy = 0, 0
        gx, gy = N-1, N-1
        # make sure top left and bottom right is empty
        if grid[sx][sy]+grid[gx][gy] != 0:
            return -1
        # 8 directions
        dx = [-1, -1, -1, 0, 0, 1, 1, 1]
        dy = [-1, 0, 1, -1, 1, -1, 0, 1]
        que = deque()
        # distance/steps
        d = [[flag for _ in range(N)] for _ in range(N)]
        # starting from point (0, 0)
        que.append((sx, sy))
        # initialization
        d[sx][sy] = 1

        while que:
            t = que.popleft()
            # if it is game point, exit
            if t[0] == gx and t[1] == gy:
                break
            # else check 8 directions
            for i in range(8):
                nx, ny = t[0]+dx[i], t[1]+dy[i]
                if 0<=nx and nx<N and 0<=ny and ny<N and grid[nx][ny]==0 \
                    and d[nx][ny]==flag:
                    que.append((nx, ny))
                    d[nx][ny] = d[t[0]][t[1]]+1
        return d[gx][gy]
        
# @lc code=end

