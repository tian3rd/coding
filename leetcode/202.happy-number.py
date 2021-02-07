#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        digit_set = set()
        while True:
            square_sum = self.digit_square_sum(n)
            if square_sum == 1:
                return True
            if square_sum not in digit_set:
                digit_set.add(square_sum)
                n = square_sum
            else:
                return False

    def digit_square_sum(self, n: int) -> int:
        rtn = 0
        while n>0:
            rtn += (n%10)**2
            n = n//10
        return rtn

        
# @lc code=end

