#
# @lc app=leetcode id=343 lang=python3
#
# [343] Integer Break
#

# @lc code=start
class Solution:
    def integerBreak(self, n: int) -> int:
        # cut rod problem (dynamic programming)
        # for the first 0, 1, 2, we can easily calculate the result
        memo = [0, 0, 1]

        for i in range(3, n+1):
            temp = 0
            for j in range(1, i):
                # we have two choices: 1. j and memo[i-j]; 2. j and i-j if the latter is bigger than divided memo array
                temp = max(temp, j*max(memo[i-j], (i-j)))
            memo.append(temp)
        return memo[n]
        
# @lc code=end

