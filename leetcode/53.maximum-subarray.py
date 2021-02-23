#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # if len(nums) == 1:
        #     return nums[0]
        # curmax, talmax = nums[0], nums[0]
        # for i in range(1, len(nums)):
        #     curmax = max(curmax+nums[i], nums[i])
        #     talmax = max(talmax, curmax)
        # return talmax

        if len(nums) == 1:
            return nums[0]
        # cases where all are negative
        if max(nums) < 0:
            return max(nums)
        # at least one positive
        tal = 0
        maxi = 0
        for i in range(len(nums)):
            tal += nums[i]
            maxi = max(maxi, tal)
            # if tally is neg, start again
            if tal < 0:
                tal = 0
        return maxi

# @lc code=end

