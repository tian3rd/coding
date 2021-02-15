#
# @lc app=leetcode id=557 lang=python3
#
# [557] Reverse Words in a String III
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split(" ")
        rtn = []
        for word in s:
            rtn.append(word[::-1])
        return " ".join(rtn)
        
# @lc code=end

