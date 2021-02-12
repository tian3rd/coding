#
# @lc app=leetcode id=415 lang=python3
#
# [415] Add Strings
#

# @lc code=start
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        rtn = ""
        carry = 0
        if len(num1) < len(num2):
            num1, num2 = num2, num1
        num2 = "0"*(len(num1)-len(num2))+num2
        print(num1, num2)
        for i in range(1, len(num1)+1):
            d_sum = int(num1[-i])+int(num2[-i])+carry
            if d_sum > 9:
                carry = 1
            else:
                carry = 0
            rtn = str(d_sum%10)+rtn
        if carry == 1:
            rtn = "1"+rtn
        return rtn
        
# @lc code=end

