#
# @lc app=leetcode id=733 lang=python3
#
# [733] Flood Fill
#

# @lc code=start
from collections import deque
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        # bfs search 4-directions
        dx = [-1, 0, 1, 0]
        dy = [0, -1, 0, 1]
        row, col = len(image), len(image[0])
        # -1 means not visited
        rtn = [[-1]*col for _ in range(row)]

        def bfs():
            q = deque()
            q.append((sr, sc))
            rtn[sr][sc] = newColor
            
            while q:
                x, y = q.popleft()
                for i in range(4):
                    nx = x+dx[i]
                    ny = y+dy[i]
                    if 0<=nx and nx<row and 0<=ny and ny<col and rtn[nx][ny]<0:
                        if image[nx][ny]==image[x][y]:
                            rtn[nx][ny] = newColor
                            # only add same color to queue
                            q.append((nx, ny))
                        else:
                            rtn[nx][ny] = image[nx][ny]
        bfs()
        # color those unvisited to original color
        for i in range(row):
            for j in range(col):
                if rtn[i][j] < 0:
                    rtn[i][j] = image[i][j]
        return rtn
        
# @lc code=end

