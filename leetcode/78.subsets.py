#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        rtn = [[]]
        if len(nums) == 0:
            return rtn
        for i in range(len(nums)):
            temp = []
            for j in range(len(rtn)):
                temp.append(rtn[j]+[nums[i]])
            rtn += temp
        return rtn
# @lc code=end

