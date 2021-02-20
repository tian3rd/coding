#
# @lc app=leetcode id=832 lang=python3
#
# [832] Flipping an Image
#

# @lc code=start
class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        for row in A:
            row[::] = row[::-1]
        r, c = len(A), len(A[0])
        for i in range(r):
            for j in range(c):
                A[i][j] = 1 - A[i][j]
        return A
# @lc code=end

