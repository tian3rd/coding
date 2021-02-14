#
# @lc app=leetcode id=448 lang=python3
#
# [448] Find All Numbers Disappeared in an Array
#

# @lc code=start
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        apperances = [True for i in range(len(nums))]
        for i in range(len(nums)):
            apperances[nums[i]-1] = False
        rtn = list()
        for ele in range(len(apperances)):
            if apperances[ele]:
                rtn.append(ele+1)
        return rtn

        # O(n) without extra space?
        
# @lc code=end

