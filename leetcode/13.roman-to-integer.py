#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        rtn = 0
        sym_value = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900,
            }
        if len(s) == 1:
            rtn += sym_value[s]
        else:
            i = 0
            while i <= len(s)-2:
                if s[i]+s[i+1] in sym_value.keys():
                    rtn += sym_value[s[i]+s[i+1]]
                    i += 2
                else: 
                    rtn += sym_value[s[i]]
                    i += 1
            if i == len(s)-1:
                rtn += sym_value[s[i]]
        return rtn
        
        
        
# @lc code=end

