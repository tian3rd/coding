#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, s: str) -> int:
        if s == '':
            return 0
        sign = 1
        start = end = index = 0
        inside_number = False
        for index in range(len(s)):
            if not inside_number:
                if s[index] == ' ':
                    continue
                elif s[index] in ['-', '+']:
                    if s[index] == '-':
                        sign = -1
                    start = index + 1
                elif ('0' <= s[index] and s[index] <= '9'):
                    start = index
                else:
                    return 0
                inside_number = True
            else:
                if not ('0' <= s[index] and s[index] <= '9'):
                    end = index
                    break
            # for case such as '42' all the way down
            if index == len(s)-1:
                end = len(s)
        # for case such as '+-12'
        if start == end: return 0
        # clamp
        rtn = sign * int(s[start:end])
        if rtn < -2**31:
            rtn = -2**31
        elif rtn > 2**31-1:
            rtn = 2**31-1
        return rtn

        
# @lc code=end

