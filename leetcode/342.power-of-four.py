#
# @lc app=leetcode id=342 lang=python3
#
# [342] Power of Four
#

# @lc code=start
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # kidding me... power of 2, 3, 4...
        if n <= 0:
            return False
        if n == 1:
            return True
        if n%4 != 0:
            return False
        else:
            return self.isPowerOfFour(n//4)
        
# @lc code=end

