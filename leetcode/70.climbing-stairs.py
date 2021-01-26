#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        # time limit exceeded
        # if n == 1 or n == 0:
        #     return 1
        # else:
        #     return self.climbStairs(n-1)+self.climbStairs(n-2)

        # use a list to store all values
        # rtn = [1, 1]
        # for i in range(2, n+1):
        #     rtn.append(rtn[i-1]+rtn[i-2])
        # return rtn[n]

        # just store 2 most recent values
        first, second = 1, 1
        for i in range(2, n+1):
            first, second = second, first+second
        return second

        
# @lc code=end

