#
# @lc app=leetcode id=746 lang=python3
#
# [746] Min Cost Climbing Stairs
#

# @lc code=start
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) < 2:
            return 0
        if len(cost) == 2:
            return min(cost)
        # use an array to store and reduce recursions
        rtn = [0, min(cost[-2:])]
        for i in range(len(cost)-3,-1,-1):
            rtn.append(min(cost[i]+rtn[-1], cost[i+1]+rtn[-2]))
        return rtn[-1]
# @lc code=end

