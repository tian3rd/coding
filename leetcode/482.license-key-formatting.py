#
# @lc app=leetcode id=482 lang=python3
#
# [482] License Key Formatting
#

# @lc code=start
class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        S = ''.join(S.split('-')).upper()
        if K >= len(S):
            return S
        m = len(S) % K
        if m == 0:
            rtn = ''
        else:
            rtn = S[:m]+'-'
        for i in range(int(len(S)//K)-1):
            rtn += S[(m+K*i):(m+K*(i+1))]+'-'
        rtn += S[-K:]
        return rtn
        
# @lc code=end

