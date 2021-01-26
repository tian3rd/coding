#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        rtn = []
        if len(a) < len(b):
            a = "0"*(len(b)-len(a)) + a
        else:
            b = "0"*(len(a)-len(b)) + b

        carry = 0
        for i in reversed(range(len(a))):
            if int(a[i])+int(b[i])+carry >= 2:
                rtn.append(int(a[i])+int(b[i])+carry-2)
                carry = 1
            else:
                rtn.append(int(a[i])+int(b[i])+carry)
                carry = 0
        if carry == 1:
            rtn.append(carry)
        rtn.reverse()
        # print(rtn)
        return ''.join(str(rtn[i]) for i in range(len(rtn)))

        
# @lc code=end

