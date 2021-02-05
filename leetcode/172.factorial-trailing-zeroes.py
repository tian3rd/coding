#
# @lc app=leetcode id=172 lang=python3
#
# [172] Factorial Trailing Zeroes
#

# @lc code=start
class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n < 5:
            return 0
        # only consider 5s in n
        twos, fives, tens = 0, 0, 0
        exp = 1
        while True:
            if n//5**exp < 1:
                 break
            else:
                fives += n//5**exp
            exp += 1    
        return fives
        
# @lc code=end

