#
# @lc app=leetcode id=793 lang=python3
#
# [793] Preimage Size of Factorial Zeroes Function
#

# @lc code=start
class Solution:
    def preimageSizeFZF(self, K: int) -> int:
        # time limit
        # target = 0
        # index = 1
        # while target <= K:
        #     if target == K:
        #         return 5
        #     target += 1
        #     extra = 0
        #     temp = index 
        #     while temp % 5 == 0:
        #         extra += 1
        #         temp //= 5
        #     target += extra
        #     index += 1
        # return 0

        # binary search 
        # for any number x, the minimum 0s is x//5 (K lower boundary), 
        # the maximux 0s is x//5 + x//25 + x//125 + ... <= x//5 * 1.25 (K upper boundary)
        # x/5 + 1 > x//5 > x/5 - 1, so we can use K to pre-determine the scope of x
        low = 4 * K - 5
        high = 5 * K + 5
        
        def countzeros(n: int):
            rtn = 0
            while n // 5 != 0:
                rtn += n // 5
                n //= 5
            return rtn
        
        while low <= high:
            mid = (low + high) // 2
            if countzeros(mid) == K:
                return 5
            elif countzeros(mid) < K:
                low = mid + 1
            else: 
                high = mid - 1
            
        return 0
# @lc code=end

