#
# @lc app=leetcode id=119 lang=python3
#
# [119] Pascal's Triangle II
#

# @lc code=start
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # if rowIndex == 0:
        #     return [1]
        # if rowIndex == 1:
        #     return [1, 1]
        # else:
        #     rtn = [1]
        #     last = self.getRow(rowIndex-1)
        #     for i in range(1, rowIndex):
        #         rtn.append(last[i-1]+last[i])
        #     rtn.append(1)
        #     return rtn

        # using O(k) space
        rtn = [0 for _ in range(rowIndex+1)]
        rtn[0] = 1

        for i in range(1, rowIndex+1):
            for j in range(i, 0, -1):
                rtn[j] += rtn[j-1]
        return rtn
# @lc code=end

