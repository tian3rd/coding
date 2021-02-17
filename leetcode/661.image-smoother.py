#
# @lc app=leetcode id=661 lang=python3
#
# [661] Image Smoother
#

# @lc code=start
class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        # 9 directions
        dx = [-1, -1, -1, 0, 0, 0, 1, 1, 1]
        dy = [-1, 0, 1, -1, 0, 1, -1, 0, 1]
        row, col = len(M), len(M[0])
        rtn = [[0]*col for _ in range(row)]
        # print(rtn)
        for i in range(row):
            for j in range(col):
                cells = 0
                for d in range(9):
                    if 0<=i+dx[d] and i+dx[d]<row \
                        and 0<=j+dy[d] and j+dy[d]<col:
                        rtn[i][j] += M[i+dx[d]][j+dy[d]]
                        cells += 1
                rtn[i][j] = int(rtn[i][j]/cells)
        # print(rtn)
        return rtn

        
# @lc code=end

