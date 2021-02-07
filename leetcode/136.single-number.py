#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # implement it with linear runtime complexity without extra memory
        # using xor: num xor num = 0; num xor 0 = num;
        rtn = 0
        for i in range(len(nums)):
            rtn = rtn ^ nums[i]
        return rtn
        
# @lc code=end

