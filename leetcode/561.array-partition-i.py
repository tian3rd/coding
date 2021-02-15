#
# @lc app=leetcode id=561 lang=python3
#
# [561] Array Partition I
#

# @lc code=start
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums = sorted(nums)
        rtn = 0
        for i in range(0, len(nums), 2):
            rtn += nums[i]
        return rtn
        
# @lc code=end

