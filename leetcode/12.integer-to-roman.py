#
# @lc app=leetcode id=12 lang=python3
#
# [12] Integer to Roman
#

# @lc code=start
class Solution:
    def intToRoman(self, num: int) -> str:
        num_lst = [
            {1: 'I', 4: 'IV', 5: 'V', 9: 'IX',},
            {1: 'X', 4: 'XL', 5: 'L', 9: 'XC',},
            {1: 'C', 4: 'CD', 5: 'D', 9: 'CM',},
            {1: 'M'}
            ]
        digit = 0
        rtn_lst = []
        while num > 0:
            mo = num % 10
            if mo in [1, 2, 3]:
                rtn_lst.append(num_lst[digit][1]*mo)
            elif mo in [4, 5, 9]:
                rtn_lst.append(num_lst[digit][mo])
            elif mo in [6, 7, 8]:
                rtn_lst.append(num_lst[digit][5]+num_lst[digit][1]*(mo-5))
            num //= 10
            digit += 1
        rtn_lst.reverse()
        return ''.join(rtn_lst)
        

        
# @lc code=end

