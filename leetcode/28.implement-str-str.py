#
# @lc app=leetcode id=28 lang=python3
#
# [28] Implement strStr()
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        if len(haystack) < len(needle):
            return -1
        for index in range(0, len(haystack)+1-len(needle)):
            if haystack[index: index+len(needle)] == needle:
                return index
        return -1
        
# @lc code=end

