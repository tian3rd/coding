#
# @lc app=leetcode id=819 lang=python3
#
# [819] Most Common Word
#

# @lc code=start
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        rtn = ''
        ban = set(banned)
        dic = dict()
        symbols = list("!?',;.")
        for sym in symbols:
            paragraph = paragraph.replace(sym, ' ')
        paragraph = paragraph.lower().split()
        print(paragraph)
        for word in paragraph:
            if word not in ban:
                if word not in dic:
                    dic[word] = 1
                else:
                    dic[word] += 1
        maxi = 0
        for word in dic:
            if dic[word]>maxi:
                maxi = dic[word]
                rtn = word
        return rtn
# @lc code=end

