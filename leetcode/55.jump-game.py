#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        if 0 not in set(nums):
            return True
        # find the rightmost occurrence of 0
        zindex = len(nums)-1-nums[::-1].index(0)
        if zindex == 0:
            return False
        for i in range(zindex-1, -1, -1):
            # if it can go past 0 or 0 is the last element
            if nums[i]+i > zindex or nums[i]+i == len(nums)-1:
                return self.canJump(nums[:i+1])
        return False
        
# @lc code=end

