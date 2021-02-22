#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        rtn = []
        # n: number of left '('s and right ')'s, indexed both with [0, n)
        # left: index of '(' to be inserted to string s, 
        # right:         ')'
        # e.g. generate(1, 0, 0, "") means we have 1 '(' and 1 ')' left, so we can insert '(' first;
        # only after sufficient '(' laying beforehead, can we insert ')' to make valid '()' pairs.
        def generate(n, left, right, s):
            if left == right and left == n:
                rtn.append(s)
                return
            if left < n:
                generate(n, left+1, right, s+'(')
            if right < left:
                generate(n, left, right+1, s+')')
        generate(n, 0, 0, "")
        return rtn
        
# @lc code=end

