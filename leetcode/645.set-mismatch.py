#
# @lc app=leetcode id=645 lang=python3
#
# [645] Set Mismatch
#

# @lc code=start
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        # use hashset to find out the duplicat O(n)
        # use the sum to calc the diff
        n = len(nums)
        diff = int(n*(n+1)/2-sum(nums))
        dic = dict()
        for i in nums:
            if i not in dic:
                dic[i] = True
            else:
                repeat = i
                break
        return [repeat, repeat+diff]
        
# @lc code=end

