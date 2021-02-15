#
# @lc app=leetcode id=541 lang=python3
#
# [541] Reverse String II
#

# @lc code=start
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s = list(s)
        for i in range(0, len(s), 2*k):
            if i+k <= len(s):
                # print(s[i:i+k])
                s[i:i+k] = s[i:i+k][::-1]
                # print(s[i:i+k])
            else:
                s[i:len(s)] = s[i:len(s)][::-1]
        return "".join(s)
        
# @lc code=end

