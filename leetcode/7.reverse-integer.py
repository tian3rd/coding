#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start

# my attempt: 
# class Solution:
#     def reverse(self, x: int) -> int:
#         sign = 1 if x >= 0 else -1
#         x *= sign
        
#         xstr = str(x)
#         xstr_reverse = ""
#         for i in range(len(xstr)):
#             xstr_reverse += xstr[len(xstr) -1 - i]
        
#         rtn = int(xstr_reverse) * sign 

#         return rtn if (-2**31 <= rtn and rtn <= 2**31-1) else 0

# alternative way: 
class Solution:
    def reverse(self, x: int) -> int:
        rtn, sign = 0, 1
        if x < 0:
            sign = -1
            x *= sign
        while x > 0:
            rtn = rtn * 10 + x % 10
            x = x // 10
        rtn *= sign
        return rtn if (-2**31 <= rtn and rtn <= 2**31-1) else 0
        
        
        
# @lc code=end

