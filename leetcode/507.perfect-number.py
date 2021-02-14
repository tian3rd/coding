#
# @lc app=leetcode id=507 lang=python3
#
# [507] Perfect Number
#

# @lc code=start
from math import sqrt
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num%2 == 1:
            return False
        divisors = [1]
        for d in range(2, int(sqrt(num))+1):
            if num%d == 0:
                divisors += [d, num//d]
        if sum(divisors) == num:
            return True
        return False
        
# @lc code=end

