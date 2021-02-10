#
# @lc app=leetcode id=268 lang=python3
#
# [268] Missing Number
#

# @lc code=start
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        rtn = (len(nums)+1)*len(nums)//2
        for i in range(len(nums)):
            rtn -= nums[i]
        return rtn
        
# @lc code=end

