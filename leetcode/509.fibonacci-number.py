#
# @lc app=leetcode id=509 lang=python3
#
# [509] Fibonacci Number
#

# @lc code=start
class Solution:
    def fib(self, n: int) -> int:
        # if n<2:
        #     return n
        # f = [0, 1]
        # for _ in range(n-1):
        #     f.append(f[-1]+f[-2])
        # return f[-1]

        # no need to create a whole list
        if n<2:
            return n
        a, b = 0, 1
        for _ in range(n-1):
            a, b = b, a+b
        return b
# @lc code=end

