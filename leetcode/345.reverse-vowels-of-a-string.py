#
# @lc app=leetcode id=345 lang=python3
#
# [345] Reverse Vowels of a String
#

# @lc code=start
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'a', 'e', 'i', 'o', 'u', 'U', 'A', 'E', 'I', 'O'}
        vowels_index = []
        for i in range(len(s)):
            if s[i] in vowels:
                vowels_index.append(i)
        s = list(s)
        for i in range(len(vowels_index)//2):
            s[vowels_index[i]], s[vowels_index[len(vowels_index)-1-i]] = \
                s[vowels_index[len(vowels_index)-1-i]], s[vowels_index[i]]
        s = "".join(s)
        return s
        
# @lc code=end

