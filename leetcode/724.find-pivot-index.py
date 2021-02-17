#
# @lc app=leetcode id=724 lang=python3
#
# [724] Find Pivot Index
#

# @lc code=start
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        right = sum(nums)
        left = 0
        nums = [0]+nums+[0]
        for pivot in range(1, len(nums)-1):
            left += nums[pivot-1]
            right -= nums[pivot]
            if left == right:
                return pivot-1
        return -1
        
# @lc code=end

