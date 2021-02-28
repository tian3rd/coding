#
# @lc app=leetcode id=1295 lang=python3
#
# [1295] Find Numbers with Even Number of Digits
#

# @lc code=start
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        rtn = 0
        for i in range(len(nums)):
            digits = 0
            while nums[i] != 0:
                digits += 1
                nums[i] //= 10
            if digits % 2 == 0:
                rtn += 1
        return rtn
        
# @lc code=end

