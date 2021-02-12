#
# @lc app=leetcode id=412 lang=python3
#
# [412] Fizz Buzz
#

# @lc code=start
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        rtn = []
        for i in range(1, n+1):
            if i%15 == 0:
                rtn.append("FizzBuzz")
                continue
            if i%5 == 0:
                rtn.append("Buzz")
                continue
            if i%3 == 0:
                rtn.append("Fizz")
                continue
            rtn.append(str(i))
        return rtn
        
# @lc code=end

