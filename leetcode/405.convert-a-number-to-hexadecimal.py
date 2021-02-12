#
# @lc app=leetcode id=405 lang=python3
#
# [405] Convert a Number to Hexadecimal
#

# @lc code=start
class Solution:
    def toHex(self, num: int) -> str:
        dic = {
            10: 'a',
            11: 'b',
            12: 'c',
            13: 'd',
            14: 'e',
            15: 'f',
        }
        rtn = ""
        if num==0:
            return "0"
        # neg + pos == 0 or overflow 2**32
        elif num<0:
            num = 2**32+num
        while num != 0:
            if num%16 > 9:
                rtn = dic[num%16]+rtn
            else:
                rtn = str(num%16)+rtn
            num //= 16
        return rtn

# @lc code=end

