#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # if digits[-1] != 9:
        #     digits[-1] += 1
        #     return digits
        # else:
        #     # ugly coding
        #     d = str(int(''.join(str(digits[i]) for i in range(len(digits)))) + 1)
        #     return list(d)
        for i in range(len(digits)-1, -1, -1):
            if digits[i] != 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
        digits[0] = 1
        digits.append(0)
        return digits

        
# @lc code=end

