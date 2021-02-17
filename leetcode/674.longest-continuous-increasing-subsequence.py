#
# @lc app=leetcode id=674 lang=python3
#
# [674] Longest Continuous Increasing Subsequence
#

# @lc code=start
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        ptr1 = 0
        maxi = 0
        while ptr1<len(nums):
            l = 1
            while ptr1+1<len(nums) and nums[ptr1]<nums[ptr1+1]:
                l += 1
                ptr1 += 1
            ptr1 += 1
            maxi = max(maxi, l)
        return maxi
        
# @lc code=end

