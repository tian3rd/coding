#
# @lc app=leetcode id=594 lang=python3
#
# [594] Longest Harmonious Subsequence
#

# @lc code=start
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        dic = dict()
        for ele in nums:
            if ele not in dic:
                dic[ele] = 1
            else:
                dic[ele] += 1
        maxi = 0
        for ele in dic:
            if ele-1 in dic and dic[ele-1]+dic[ele]>maxi:
                maxi = dic[ele-1]+dic[ele]
            if ele+1 in dic and dic[ele+1]+dic[ele]>maxi:
                maxi = dic[ele+1]+dic[ele]
            # maxi = max(maxi, dic[ele])
        return maxi
        
# @lc code=end

