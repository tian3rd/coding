class Solution:
    def maximumScore(self, nums, multipliers) -> int:
        # time limit
        # def ms(nums, muls):
        #     if len(muls) == 1:
        #         return max(muls[0]*nums[0], muls[0]*nums[-1])
        #     else:
        #         return max(muls[0]*nums[0]+ms(nums[1:], muls[1:]), muls[0]*nums[-1]+ms(nums[:-1], muls[1:]))
        # return ms(nums, multipliers)

        # self.rtn = [[float('-inf') for _ in range(len(multipliers))] for _ in range(len(multipliers))]

        # def helper(nums, multipliers, i, j):
        #     if self.rtn[i][j] != float('-inf'):
        #         return self.rtn[i][j]
        #     if i+j == len(multipliers):
        #         return 0
        #     self.rtn[i][j] = max(nums[i] * multipliers[i+j] + helper(nums, multipliers, i+1, j), \
        #         nums[len(nums)-1-j] * multipliers[i+j] + helper(nums, multipliers, i, j+1))
        #     return self.rtn[i][j]

        # return helper(nums, multipliers, 0, 0)

        n, m = len(nums), len(multipliers)
        dp = [[0]*(m+1) for _ in range(m+1)]
        for i in range(m, -1, -1):
            for j in range(m-i, -1, -1):
                if i+j == m:
                    dp[i][j] = 0
                else:
                    dp[i][j] = max(dp[i+1][j]+multipliers[i+j]*nums[i], dp[i][j+1]+multipliers[i+j]*nums[n-1-j])
        return dp[0][0]
