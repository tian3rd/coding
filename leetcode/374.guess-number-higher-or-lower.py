#
# @lc app=leetcode id=374 lang=python3
#
# [374] Guess Number Higher or Lower
#

# @lc code=start
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        # this is binary search example
        low, high = 1, n
        while low<=high:
            mid = (low+high)//2
            right = guess(mid)
            if right == 0:
                return mid
            elif right < 0:
                high = mid-1
            else:
                low = mid+1
        
# @lc code=end

