#
# @lc app=leetcode id=1720 lang=python3
#
# [1720] Decode XORed Array
#

# @lc code=start
class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        rtn = [first]
        for num in encoded:
            rtn.append(num ^ first)
            first = rtn[-1]
        return rtn
        
# @lc code=end

