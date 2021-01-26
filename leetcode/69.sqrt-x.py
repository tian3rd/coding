#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        # O(n) time
        # if x == 0 or x == 1:
        #     return x
        # for i in range(x+1):
        #     if i*i > x:
        #         return i-1

        # O(lgn)
        if x < 2:
            return x

        left, right = 1, x // 2
        while left <= right:
            mid = left + (right - left) // 2
            if mid > x / mid:
                right = mid - 1
            else:
                left = mid + 1

        return left - 1
        
# @lc code=end

