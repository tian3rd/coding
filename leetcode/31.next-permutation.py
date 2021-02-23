#
# @lc app=leetcode id=31 lang=python3
#
# [31] Next Permutation
#

# @lc code=start
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums)==1:
            return nums
        # for i in range(len(nums)-1, 0, -1):
        #     if nums[i]>nums[i-1]:
        #         nums[i], nums[i-1] = nums[i-1], nums[i]
        #         return
        # first, find the one which is larger than the former, 1 2 5 4 3 0, i.e 5, the #s after 5 is descended
        # binary search the position for 2 to be inserted, i.e, after 3, then switch 2 and 3, reverse the rest 
        # to follow: 1 3 0245
        
        
        
# @lc code=end

