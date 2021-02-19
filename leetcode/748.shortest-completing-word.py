#
# @lc app=leetcode id=748 lang=python3
#
# [748] Shortest Completing Word
#

# @lc code=start
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        def count_letters(string: str) -> dict:
            dic = dict()
            for letter in string.lower():
                if letter < 'a' or letter > 'z':
                    continue
                if letter not in dic:
                    dic[letter] = 1
                else:
                    dic[letter] += 1
            return dic
        lp = count_letters(licensePlate)
        print(lp)
        rtn = words[0]
        small = 16
        for word in words:
            wdic = count_letters(word)
            is_smallest = True
            for l in lp:
                if l not in wdic or (l in wdic and lp[l]>wdic[l]):
                    is_smallest = False
                    break

            if is_smallest and len(word)<small:
                small = len(word)
                rtn = word
        return rtn

        
# @lc code=end

