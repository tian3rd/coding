#
# @lc app=leetcode id=824 lang=python3
#
# [824] Goat Latin
#

# @lc code=start
class Solution:
    def toGoatLatin(self, S: str) -> str:
        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        rtn = []
        S = S.split()
        for i in range(len(S)):
            if S[i][0] in vowels:
                s = S[i][:]
            else:
                s = (S[i][1:]+S[i][0])
            s += 'ma' + 'a'*(i+1)
            rtn.append(s)
        return ' '.join(rtn)
        
# @lc code=end

