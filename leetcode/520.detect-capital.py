#
# @lc app=leetcode id=520 lang=python3
#
# [520] Detect Capital
#

# @lc code=start
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) == 1:
            return True
        if word == word.upper() or word == word.lower():
            return True
        if word[0] == word[0].upper():
            if word[1:].lower() == word[1:]:
                return True
            else:
                return False
        return False
        
        
# @lc code=end

