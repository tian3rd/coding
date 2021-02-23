#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        rtn = []
        def permutation(nums, start, end):
            if start == end:
                rtn.append(nums)
                return
            for i in range(start, end+1):
                nums[start], nums[i] = nums[i], nums[start]
                # why permutations(nums, start+1, end) does not work?
                permutation(nums[:], start+1, end)
                nums[start], nums[i] = nums[i], nums[start]
        permutation(nums, 0, n-1)
        return rtn
        
# @lc code=end

