#
# @lc app=leetcode id=680 lang=python3
#
# [680] Valid Palindrome II
#

# @lc code=start
class Solution:
    def validPalindrome(self, s: str) -> bool:
        if len(s) <= 2:
            return True
        left, right = 0, len(s)-1
        while left<right and s[left] == s[right]:
            left += 1
            right -= 1
        if left >= right:
            return True
        if s[left+1]!=s[right] and s[left]!=s[right-1]:
            return False
        return s[left+1:right+1][::-1]==s[left+1:right+1] or s[left:right][::-1]==s[left:right]
# @lc code=end

if __name__ == '__main__':
    s = "aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"
    print()

