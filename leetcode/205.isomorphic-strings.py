#
# @lc app=leetcode id=205 lang=python3
#
# [205] Isomorphic Strings
#

# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic = dict()
        for i in range(len(s)):
            if s[i] not in dic.keys():
                # edge case 'badc' 'baba'
                if t[i] in dic.values():
                    return False
                dic[s[i]] = t[i]
            else:
                if dic[s[i]] != t[i]:
                    return False
        return True
        
# @lc code=end

