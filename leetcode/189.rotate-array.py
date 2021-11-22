#
# @lc app=leetcode id=189 lang=python3
#
# [189] Rotate Array
#

# @lc code=start
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        for i in range(k):
            # nums[i], nums[i+k], nums[n-k-1+i] = nums[i+k], nums[n-k-1+i], nums[i]
            nums.insert(0, nums.pop())
        # nums[:] = nums[n-k:] + nums[:n-k]
        
        
# @lc code=end

