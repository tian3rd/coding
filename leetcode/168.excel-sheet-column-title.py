#
# @lc app=leetcode id=168 lang=python3
#
# [168] Excel Sheet Column Title
#

# @lc code=start

import string
class Solution:
    def convertToTitle(self, n: int) -> str:
        rtn = ""
        numbers = [i for i in range(1, 26)]
        numbers.append(0)
        letters = string.ascii_uppercase
        dic = dict(zip(numbers, letters))
        while n > 0:
            m = n % 26
            rtn = dic[m] + rtn
            if m == 0:
                n = n // 26 - 1
            else:
                n = n // 26
            
        return rtn
        
# @lc code=end

