#
# @lc app=leetcode id=784 lang=python3
#
# [784] Letter Case Permutation
#

# @lc code=start
class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        # if len(S) == 1:
        #     if S.isalpha():
        #         return [S.lower(), S.upper()]
        #     else:
        #         return [S]
        # else:
        #     if S
        
        rtn = [""]
        for i in range(len(S)):
            if S[i].isnumeric():
                rtn = [s+S[i] for s in rtn]
            else:
                rtn = [s+S[i].upper() for s in rtn] +  [s+S[i].lower() for s in rtn]
        return rtn

# @lc code=end

