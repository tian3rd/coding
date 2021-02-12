#
# @lc app=leetcode id=409 lang=python3
#
# [409] Longest Palindrome
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> int:
        # deal with odd apperances
        rtn = 0
        anyodd = False
        dic = dict()
        for i in range(len(s)):
            if s[i] not in dic:
                dic[s[i]] = 1
            else:
                dic[s[i]] += 1
        for letter in dic:
            if dic[letter]%2 == 0:
                rtn += dic[letter]
            else:
                anyodd = True
                rtn += dic[letter]-1
        if anyodd:
            rtn += 1
        return rtn
        
# @lc code=end

