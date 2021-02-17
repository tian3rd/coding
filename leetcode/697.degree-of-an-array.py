#
# @lc app=leetcode id=697 lang=python3
#
# [697] Degree of an Array
#

# @lc code=start
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        dic = dict()
        maxi = 0
        lst = []
        for n in nums:
            if n in dic:
                dic[n] += 1
            else:
                dic[n] = 1
            if maxi < dic[n]:
                lst = [n]
                maxi = dic[n]
            elif maxi == dic[n]:
                lst.append(n)
        # print(lst)
        rtn = len(nums)
        for n in lst:
            left, right = 0, len(nums)-1
            while nums[left] != n:
                left += 1
            while nums[right] != n:
                right -= 1
            rtn = min(rtn, right-left+1)
        return rtn

        
        
# @lc code=end

