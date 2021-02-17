#
# @lc app=leetcode id=665 lang=python3
#
# [665] Non-decreasing Array
#

# @lc code=start
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        if len(nums)<3:
            return True
        modified = False
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                if modified:
                    return False
                else:
                    modified = True
                    # two ways to modify, both need to check
                    if 1<=i and i<=len(nums)-3 and nums[i-1]>nums[i+1] and nums[i]>nums[i+2]:
                        return False
        return True

# @lc code=end

