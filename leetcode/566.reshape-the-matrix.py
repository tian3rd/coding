#
# @lc app=leetcode id=566 lang=python3
#
# [566] Reshape the Matrix
#

# @lc code=start
class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        row, col = len(nums), len(nums[0])
        if (row * col) != (r * c):
            return nums
        longlst = [nums[i][j] for i in range(row) for j in range(col)]
        rtn = []
        for i in range(r):
            rtn.append(longlst[i*c:(i+1)*c])
        return rtn
            

        
# @lc code=end

