#
# @lc app=leetcode id=1313 lang=python3
#
# [1313] Decompress Run-Length Encoded List
#

# @lc code=start
class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        rtn = []
        for i in range(0, len(nums), 2):
            rtn += [nums[i+1]]*nums[i]
        return rtn
    
        
# @lc code=end

