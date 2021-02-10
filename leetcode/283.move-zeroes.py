#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # zeros = 0
        # for i in range(len(nums)):
        #     if nums[i] == 0:
        #         zeros += 1
        # for i in range(len(nums)-zeros):
        #     for j in range(i, len(nums)):
        #         if nums[j] != 0:
        #             nums[i], nums[j] = nums[j], nums[i]
        #             break
        
        # two pointers: 
        # pt1 points to the tail of non-zero elements;
        # pt2 points to the head of the rest non-zeros;
        pt1 = 0
        for pt2 in range(len(nums)):
            if nums[pt2] != 0:
                nums[pt1] = nums[pt2]
                pt1 += 1
        for i in range(pt1, len(nums)):
            nums[i] = 0
# @lc code=end

