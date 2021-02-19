#
# @lc app=leetcode id=747 lang=python3
#
# [747] Largest Number At Least Twice of Others
#

# @lc code=start
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        lar = max(nums)
        sec = float('-inf')
        for i in range(len(nums)):
            if nums[i] == lar:
                index = i
            elif nums[i]>sec:
                sec = nums[i]
        if lar>=2*sec:
            return index
        return -1
        
# @lc code=end

