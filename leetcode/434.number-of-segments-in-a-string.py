#
# @lc app=leetcode id=434 lang=python3
#
# [434] Number of Segments in a String
#

# @lc code=start
class Solution:
    def countSegments(self, s: str) -> int:
        # segs = set(list("!@#$%^&*()_+-=',.: "))
        # rtn = 0
        # for i in range(len(s)):
        #     if s[i] in segs:
        #         rtn += 1
        # return rtn
        if s == "":
            return 0
        lst = s.split(" ")
        rtn = 0
        for i in range(len(lst)):
            if lst[i] != '':
                rtn += 1
        return rtn
        # how to eliminate leading and trailing spaces?
        
# @lc code=end

