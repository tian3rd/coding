#
# @lc app=leetcode id=1249 lang=python3
#
# [1249] Minimum Remove to Make Valid Parentheses
#

# @lc code=start
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        rtn = ''
        q = list()
        remove = set()
        for i in range(len(s)):
            if s[i] == '(':
                q.append(i)
            elif s[i] == ')':
                if len(q) == 0:
                    remove.add(i)
                else:
                    q.pop()
        for i in q:
            remove.add(i)
        for i in range(len(s)):
            if i not in remove:
                rtn += s[i]
        return rtn


        
# @lc code=end

