#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#

# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        rtn = set()
        def permutation(nums, start, end):
            if start == end:
                rtn.add(' '.join([str(i) for i in nums]))
                return
            for i in range(start, end+1):
                nums[start], nums[i] = nums[i], nums[start]
                # why permutations(nums, start+1, end) does not work?
                permutation(nums[:], start+1, end)
                nums[start], nums[i] = nums[i], nums[start]
        permutation(nums, 0, n-1)

        res = [list(element.split()) for element in rtn]
        return res
        
# @lc code=end

