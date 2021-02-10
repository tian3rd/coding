#
# @lc app=leetcode id=290 lang=python3
#
# [290] Word Pattern
#

# @lc code=start
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_lst = s.split(" ")
        if len(pattern) != len(s_lst):
            return False
        dic = dict()
        for i in range(len(pattern)):
            if pattern[i] not in dic.keys():
                # check against case like: abba -- dog dog dog dog
                if s_lst[i] in dic.values():
                    return False
                dic[pattern[i]] = s_lst[i]
            elif dic[pattern[i]] != s_lst[i]:
                return False
        return True
        
# @lc code=end

