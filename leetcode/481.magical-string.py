#
# @lc app=leetcode id=481 lang=python3
#
# [481] Magical String
#

# @lc code=start
class Solution:
    def magicalString(self, n: int) -> int:
        '''
        try again. use head and tail to track the string.
        '''
        s = [1, 2, 2]
        rtn = 1
        if n <= 0:
            return 0
        if n <= 3:
            return 1
        # head points to the 3rd ele
        head = 2
        rtn = 1
        while len(s) < n:
            # to switch between 1 and 2, s[-1] tracks the tail
            added = s[-1] ^ 3
            s.append(added)
            if s[head] == 2:
                s.append(s[-1])
            if added == 1:
                rtn += s[head]
            head += 1
        # if added 2 elements instead of 1, check the added ele
        if len(s) == n:
            return rtn
        if len(s) > n:
            if s[-1] == 2:
                return rtn
            else:
                return rtn-1
        
        
# @lc code=end

