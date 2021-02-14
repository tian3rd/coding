#
# @lc app=leetcode id=485 lang=python3
#
# [485] Max Consecutive Ones
#

# @lc code=start
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ptr, maxi = 0, 0
        while True:
            if ptr >= len(nums):
                return maxi
            n = 0
            if nums[ptr] == 0:
                ptr += 1
                continue
            else:
                while ptr+n <= len(nums)-1 and nums[ptr+n] == 1:
                    n += 1
                if n > maxi:
                    maxi = n
                ptr += n+1
        
        
# @lc code=end

