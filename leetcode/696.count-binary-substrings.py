#
# @lc app=leetcode id=696 lang=python3
#
# [696] Count Binary Substrings
#

# @lc code=start
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        arr = []
        ptr = 0
        while ptr <= len(s)-1:
            i = 1
            while ptr+i <= len(s)-1 and s[ptr]==s[ptr+i]:
                i += 1
            arr.append(i)
            ptr += i
        rtn = 0
        for i in range(len(arr)-1):
            rtn += min(arr[i], arr[i+1])
        return rtn

        
# @lc code=end

