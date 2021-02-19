#
# @lc app=leetcode id=762 lang=python3
#
# [762] Prime Number of Set Bits in Binary Representation
#

# @lc code=start
class Solution:
    def countPrimeSetBits(self, L: int, R: int) -> int:
        rtn = 0
        primes = set([2, 3, 5, 7, 11, 13, 17, 19])
        for num in range(L, R+1):
            if bin(num).count("1") in primes:
                rtn += 1
        return rtn
        
# @lc code=end

