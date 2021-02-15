#
# @lc app=leetcode id=551 lang=python3
#
# [551] Student Attendance Record I
#

# @lc code=start
class Solution:
    def checkRecord(self, s: str) -> bool:
        if len(s) == 1:
            return True
        na, ptr = 0, 0
        while ptr < len(s):
            if s[ptr] == 'A':
                na += 1
                if na>1:
                    return False
            elif s[ptr] == 'L':
                if ptr<len(s)-2 and s[ptr:ptr+3]=='LLL':
                    return False
            ptr += 1
        return True

        
# @lc code=end

