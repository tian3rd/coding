#
# @lc app=leetcode id=542 lang=python3
#
# [542] 01 Matrix
#

# @lc code=start
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # time limit exceeded!!
        # rtn = [[0 for _ in range(len(mat[0]))] for _ in range(len(mat))]
        # for i in range(len(mat)):
        #     for j in range(len(mat[0])):
        #         if mat[i][j] == 0:
        #             rtn[i][j] = 0
        #         else:
        #             q = []
        #             visited = [[False for _ in range(len(mat[0]))] for _ in range(len(mat))]
        #             q.append([i, j])
        #             visited[i][j] = True
        #             rtn[i][j] = 0
        #             surrounded = True
        #             while q and surrounded:
        #                 rtn[i][j] += 1
        #                 sz = len(q)
        #                 for _ in range(sz):
        #                     x, y = q.pop(0)
        #                     for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
        #                         nx, ny = x + dx, y + dy
        #                         if 0 <= nx < len(mat) and 0 <= ny < len(mat[0]) and not visited[nx][ny]:
        #                             if mat[nx][ny] == 1:
        #                                 q.append([nx, ny])
        #                                 visited[nx][ny] = True
        #                             else:
        #                                 surrounded = False
        # return rtn

        # "Start from each 0, find the distance between this 0 and each no-zero element. update the distance if the distance is shorter than the current."
        # from https://zhenyu0519.github.io/2020/03/19/lc542/
        rtn = [[0 for _ in range(len(mat[0]))] for _ in range(len(mat))]
        q = collections.deque()
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    # first append all 0 elements to the queue
                    q.append([i, j])
                else:
                    rtn[i][j] = float('inf')
        # the first round, update all 1s next to 0s; the next round, update the second layer of 1s (which are not directly connected with 0s, but with the first layer of 1s), so on and so forth
        while q:
            x, y = q.popleft()
            for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(mat) and 0 <= ny < len(mat[0]) and rtn[nx][ny] > rtn[x][y] + 1:
                    rtn[nx][ny] = rtn[x][y] + 1
                    q.append([nx, ny])
        return rtn


        
# @lc code=end

