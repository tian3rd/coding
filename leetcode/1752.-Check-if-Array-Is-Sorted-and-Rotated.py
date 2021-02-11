#
# @lc app=leetcode id=1752 lang=python3
#
# [1752] Check if Array Is Sorted and Rotated
#

# @lc code=start
class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 1:
            return True
        i = 0
        while i <= len(nums)-2:
            if nums[i+1] < nums[i]:
                break
            i += 1
        # sorted array
        if i == len(nums)-1:
            return True
        # rotated, make sure first ele is less than/equal the smallest
        if nums[i+1] > nums[0]:
            return False
        for p in range(i+1, len(nums)-1):
            # can not rotate again
            if nums[p+1] < nums[p]:
                return False
            # every element should be less than/equal 
            if nums[p+1]>nums[0]:
                return False
        return True