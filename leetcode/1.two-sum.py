#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            dic[nums[i]] = i
        for i in range(len(nums)):
            if target-nums[i] in dic.keys():
                # check for duplicates
                if target != 2 * nums[i]:
                    return [i, dic[target-nums[i]]]
                elif i != dic[target-nums[i]]:
                    return [i, dic[nums[i]]]
        

        
# @lc code=end

