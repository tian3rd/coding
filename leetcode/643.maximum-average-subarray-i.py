#
# @lc app=leetcode id=643 lang=python3
#
# [643] Maximum Average Subarray I
#

# @lc code=start
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if len(nums) == k:
            return sum(nums)/k
        tal = sum(nums[:k])
        maxi = tal
        # for i in range(len(nums)-k+1):
        #     maxi = max(maxi, sum(nums[i:i+k]))
        # return maxi/k
        for i in range(k,len(nums)):
            tal += nums[i]-nums[i-k]
            maxi = max(maxi, tal)
        return maxi/k
        
# @lc code=end

