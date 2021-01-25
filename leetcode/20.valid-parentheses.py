#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        # using stack
        length = len(s)
        if length % 2 == 1:
            return False
        left_bracket = ["(", "[", "{"]
        right_bracket = {")": "(", "]": "[", "}": "{"}
        stack = []
        for i in range(length):
            if s[i] in left_bracket:
                stack.append(s[i])
            if s[i] in right_bracket.keys():
                if len(stack) == 0 or stack[-1] != right_bracket[s[i]]:
                    return False
                else:
                    stack.pop()
        if len(stack) == 0:
            return True
        else:
            return False

        
        
# @lc code=end

