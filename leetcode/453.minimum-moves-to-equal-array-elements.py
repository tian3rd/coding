#
# @lc app=leetcode id=453 lang=python3
#
# [453] Minimum Moves to Equal Array Elements
#

# @lc code=start
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        rtn = 0
        if len(set(nums)) == 1:
            return 0
        nums = sorted(nums)
        mini, maxi = nums[0], nums[-1]
        for i in range(2, len(nums)+1):
            rtn += maxi-mini
            maxi = nums[-i]
        return rtn

# @lc code=end

