#
# @lc app=leetcode id=476 lang=python3
#
# [476] Number Complement
#

# @lc code=start
class Solution:
    def findComplement(self, num: int) -> int:
        b = list(bin(num))
        for i in range(2, len(b)):
            if b[i] == '0':
                b[i] = '1'
            else:
                b[i] = '0'
        return int(''.join(b),2)    
        
        # how to use ~ for binary numbers?
# @lc code=end

