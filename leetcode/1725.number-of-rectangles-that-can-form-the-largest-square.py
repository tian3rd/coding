#
# @lc app=leetcode id=1725 lang=python3
#
# [1725] Number Of Rectangles That Can Form The Largest Square
#

# @lc code=start
class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        maxi = 0
        rtn = 0
        for rec in rectangles:
            if min(rec) > maxi:
                maxi = min(rec)
                rtn = 1
            elif min(rec) == maxi:
                rtn += 1
        return rtn
# @lc code=end

