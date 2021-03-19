#
# @lc app=leetcode id=1632 lang=python3
#
# [1632] Rank Transform of a Matrix
#

# @lc code=start
class Solution:
    def matrixRankTransform(self, matrix: List[List[int]]) -> List[List[int]]:
        # row, col = len(matrix), len(matrix[0])
        # lst = []
        # for l in matrix:
        #     lst += l
        # lst = sorted(lst)
        # dic = dict()
        # for i in range(len(lst)):
        #     if lst[i] not in dic:
        #         dic[lst[i]] = i
        # rtn = [[0 for _ in range(col)] for _ in range(row)]
        # for i in range(row):
        #     for j in range(col):
        #         rtn[i][j] = dic[matrix[i][j]]
        # return rtn
# @lc code=end

