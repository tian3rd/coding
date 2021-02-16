#
# @lc app=leetcode id=598 lang=python3
#
# [598] Range Addition II
#

# @lc code=start
class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        if ops == []:
            return m*n
        minix = max(m,n)+1
        miniy = minix
        for op in ops:
            minix = min(op[0], minix)
            miniy = min(op[1], miniy)
        return minix*miniy
        
# @lc code=end

