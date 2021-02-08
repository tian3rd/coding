#
# @lc app=leetcode id=228 lang=python3
#
# [228] Summary Ranges
#

# @lc code=start
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        rtn = []
        if len(nums) == 0:
            return rtn
        elif len(nums) == 1:
            rtn.append(str(nums[0]))
            return rtn
        first, second = 0, 0

        while second < len(nums):
            while nums[first] + (second-first) == nums[second]:
                second += 1
                # beware of index out of range
                if second == len(nums):
                    break
            if first == second-1:
                rtn.append(str(nums[first]))
            else:
                rtn.append("{}{}{}".format(nums[first],"->",nums[second-1]))
            first = second

        return rtn
        
# @lc code=end

