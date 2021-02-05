#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums_set = set(nums)
        dic = dict(zip(nums_set, [0]*len(nums_set)))
        for i in range(len(nums)):
            dic[nums[i]] += 1
        times, rtn = 0, 0
        for key in dic.keys():
            if dic[key] > times:
                times = dic[key]
                rtn = key
        return rtn

        
# @lc code=end

