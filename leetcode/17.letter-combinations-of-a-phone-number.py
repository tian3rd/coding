#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        dic = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz",
        }
        rtn = []
        self.backtrack(rtn, "", 0, digits, dic)
        return rtn
    
    def backtrack(self, rtn: List[str], word: str, index: int, digits: str, dic):
        # end state
        if index == len(digits):
            rtn.append(word)
            return
        for l in dic[digits[index]]:
            word += l
            self.backtrack(rtn, word, index+1, digits, dic)
            # backtrack to initial state
            word = word[:-1]

        
# @lc code=end

