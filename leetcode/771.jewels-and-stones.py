#
# @lc app=leetcode id=771 lang=python3
#
# [771] Jewels and Stones
#

# @lc code=start
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        def count_letters(string: str) -> dict:
            dic = dict()
            for l in string:
                if l not in dic:
                    dic[l] = 1
                else:
                    dic[l] += 1
            return dic
        s = count_letters(stones)
        rtn = 0
        jw = set(list(jewels))
        for element in s:
            if element in jw:
                rtn += s[element]
        return rtn 
        
# @lc code=end

