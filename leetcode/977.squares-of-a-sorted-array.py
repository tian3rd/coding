#
# @lc app=leetcode id=977 lang=python3
#
# [977] Squares of a Sorted Array
#

# @lc code=start
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        if nums[0] >= 0:
            return [n**2 for n in nums]
        elif nums[-1] <= 0:
            return [nums[i]**2 for i in range(len(nums)-1, -1, -1)]
        else:
            rtn = []
            left, right = 0, 0
            for i in range(len(nums)-1):
                if nums[i] * nums[i+1] <= 0:
                    left = i
                    right = i + 1
                    break
            for i in range(len(nums)):
                if left >= 0 and right <= len(nums)-1:
                    if abs(nums[left]) <= nums[right]:
                        rtn.append(nums[left]**2)
                        left -= 1
                    else:
                        rtn.append(nums[right]**2)
                        right += 1
                elif left < 0:
                    rtn.append(nums[right]**2)
                    right += 1
                else:
                    rtn.append(nums[left]**2)
                    left -= 1
            return rtn

        
# @lc code=end

