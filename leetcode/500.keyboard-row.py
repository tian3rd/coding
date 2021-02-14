#
# @lc app=leetcode id=500 lang=python3
#
# [500] Keyboard Row
#

# @lc code=start
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows = (set("qwertyuiop"), set("asdfghjkl"), set("zxcvbnm"))
        rtn = list()
        for word in words:
            for row in rows:
                if set(word.lower()).issubset(row):
                    rtn.append(word)
                    break
        return rtn
        
# @lc code=end

