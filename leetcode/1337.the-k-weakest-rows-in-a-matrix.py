#
# @lc app=leetcode id=1337 lang=python3
#
# [1337] The K Weakest Rows in a Matrix
#

# @lc code=start
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        rank = [(sum(mat[row]), row) for row in range(len(mat))]
        rank = sorted(rank)
        rtn = list()
        for i in range(k):
            rtn.append(rank[i][1])
        return rtn
        
# @lc code=end

