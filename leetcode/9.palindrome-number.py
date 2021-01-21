#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
# my attempt 1
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
           return False
        x_list = []
        while x > 0:
            x_list.append(x % 10)
            x //= 10
        for i in range(len(x_list)//2):
            if x_list[i] != x_list[len(x_list)-1-i]: 
                return False
        return True

# my attempt 2
# class Solution:
#     def isPalindrome(self, x: int) -> bool:
# @lc code=end

