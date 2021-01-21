#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
# my attempt
class Solution:
    def longestPalindrome(self, s: str) -> str:
        span, middle, max_span = 1, 0, 0
        if len(s) == 1 or len(set(list(s))) == 1: 
            return s
        s = " " + " ".join(list(s)) + " "
        for i in range(1, len(s)-1):
            while i-(span+1)>=0 and i+(span+1)<=len(s)-1 and s[i-span-1]==s[i+span+1]:
                span += 1
            if span > max_span:
                middle = i
                max_span = span
            # need to reset span to 0
            span = 0
        rtn = "".join(s[middle-max_span:middle+max_span+1].split(" "))
        return rtn

# 
# @lc code=end

