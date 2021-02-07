#
# @lc app=leetcode id=204 lang=python3
#
# [204] Count Primes
#

# @lc code=start
class Solution:
    def countPrimes(self, n: int) -> int:
        if n<=2:
            return 0
        # Sieve of Eratosthenes
        list_primes = [True for _ in range(n)]
        list_primes[0] = list_primes[1] = False
        # print(list_primes)
        for i in range(int(n**0.5)+1):
            if list_primes[i] == True:
                # note: start from i^2, increment by i
                for j in range(i**2, n, i):
                    list_primes[j] = False
        # print(list_primes)
        rtn = 0
        for e in list_primes:
            if e == True:
                rtn += 1
        return rtn
# @lc code=end

