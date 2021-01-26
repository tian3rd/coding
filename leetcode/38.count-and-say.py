#
# @lc app=leetcode id=38 lang=python3
#
# [38] Count and Say
#

# @lc code=start
class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1: 
            return "1"
        else: 
            rtn = ""
            index = 0
            # recursion
            say = self.countAndSay(n-1)
            while index < len(say):
                # re-initialize # of the current index sym_value
                num_index = 1
                while index+num_index < len(say) \
                    and say[index] == say[index+num_index]:
                    num_index += 1
                rtn += str(num_index) + say[index]
                index += num_index
            return rtn

    # def countAndSay(self, n: int) -> int:
    #     # use a list to store calculated results.
    #     say_list = ["1"]
    #     for _ in range(n):
    #         say = say_list[-1]
    #         rtn = ""
    #         index = 0
    #         while index < len(say):
    #             num_index = 1
    #             while index+num_index < len(say) \
    #                 and say[index] == say[index+num_index]:
    #                 num_index += 1
    #             rtn += str(num_index) + say[index]
    #             index += num_index
    #         say_list.append(rtn)
    #     return say_list[n-1]

# @lc code=end

