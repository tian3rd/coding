#
# @lc app=leetcode id=509 lang=python3
#
# [509] Fibonacci Number
#

# @lc code=start
class Solution:
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        rtn = [0, 1]
        for _ in range(2, n + 1):
            rtn.append(rtn[-1] + rtn[-2])
        return rtn[-1]
        
# @lc code=end

