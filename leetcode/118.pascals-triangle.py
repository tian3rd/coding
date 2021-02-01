#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#

# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
    #     rtn = []
    #     for i in range(numRows):
    #         rtn.append(self.row_list(i))
    #     return rtn

    # def row_list(self, row_no: int) -> List[int]:
    #     if row_no == 0:
    #         return [1]
    #     factorial_list = self.factorial(row_no)
    #     rtn = []
    #     for i in range(0, row_no+1):
    #         rtn.append(int(factorial_list[row_no]/(factorial_list[row_no-i]*factorial_list[i])))
    #     return rtn

    # def factorial(self, num: int) -> List[int]:
    #     if num == 0:
    #         return [1]
    #     if num == 1:
    #         return [1, 1]
    #     else:
    #         rtn = self.factorial(num-1)
    #         rtn.append(self.factorial(num-1)[-1]*num)
    #         return rtn

    # use the method described in the problem
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1,1]]
        else:
            rtn = self.generate(numRows-1)
            # first create a list
            rtn.append([1])
            for i in range(1, numRows-1):
                rtn[-1].append(rtn[-2][i-1]+rtn[-2][i])
            # remember to add 1 to the end
            rtn[-1].append(1)
            return rtn

# @lc code=end

