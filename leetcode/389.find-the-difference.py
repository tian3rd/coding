#
# @lc app=leetcode id=389 lang=python3
#
# [389] Find the Difference
#

# @lc code=start
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # one way is hashset or dictionary
        dic_t = dict()
        for i in range(len(t)):
            if t[i] not in dic_t:
                dic_t[t[i]] = 1
            else:
                dic_t[t[i]] += 1
        for i in range(len((s))):
            dic_t[s[i]] -= 1
        for key in dic_t.keys():
            if dic_t[key] == 1:
                return key
        
# @lc code=end

