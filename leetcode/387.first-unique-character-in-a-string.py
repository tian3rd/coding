#
# @lc app=leetcode id=387 lang=python3
#
# [387] First Unique Character in a String
#

# @lc code=start
class Solution:
    def firstUniqChar(self, s: str) -> int:
        # still a dictionary
        dic = dict()
        for i in range(len(s)):
            if s[i] not in dic:
                dic[s[i]] = True
            else:
                dic[s[i]] = False
        for i in range(len(s)):
            if dic[s[i]] is True:
                return i
        return -1
        
# @lc code=end

