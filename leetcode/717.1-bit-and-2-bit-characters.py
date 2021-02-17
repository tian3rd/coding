#
# @lc app=leetcode id=717 lang=python3
#
# [717] 1-bit and 2-bit Characters
#

# @lc code=start
class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        if bits == [0] or bits == []:
            return True
        if bits == [1, 0]:
            return False
        if bits[0] == 1:
            return self.isOneBitCharacter(bits[2:])
        return self.isOneBitCharacter(bits[1:])
        
# @lc code=end

