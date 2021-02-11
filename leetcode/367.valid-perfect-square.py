#
# @lc app=leetcode id=367 lang=python3
#
# [367] Valid Perfect Square
#

# @lc code=start
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 0:
            return False
        if num == 0:
            return True
        # check last digit
        if num%10 not in {0, 1, 4, 5, 6, 9}:
            return False
        # # check # of digits
        # n = num
        # n_dig = 1
        # while n != 0:
        #     n_dig += 1
        #     n //= 10
        # 
        # Ugly
        # n = num
        # first_dig, total_dig = 1, 0
        # while n != 0:
        #     total_dig += 1
        #     if n // 10 == 0:
        #         first_dig = n%10
        #     n //= 10
        # dic = {
        #     1: 1,
        #     2: 1,
        #     3: 1,
        #     4: 2,
        #     5: 2, 
        #     6: 2,
        #     7: 2,
        #     8: 2,
        #     9: 3
        # }
        # if total_dig%2 == 0:
        #     for i in range(dic[first_dig]*10**(total_dig//2-1), 10**(total_dig//2+1)):
        #         if num%i == 0:
        #             if num//i == i:
        #                 return True
        #             if i > num//i:
        #                 return False
        # else:
        #     for i in range(dic[first_dig]*10**(total_dig//2), (dic[first_dig]+1)*10**(total_dig//2)):
        #         if num%i == 0:
        #             if num//i == i:
        #                 return True
        #             if i > num//i:
        #                 return False
        
        # 2nd solution: 1+3+...+(2n-1) == n^2
        # if num == 0:
        #     return True
        # sum_num = 0
        # while True:
        #     for i in range(1, num+1, 2):
        #         sum_num += i
        #         if sum_num == num:
        #             return True
        #         elif sum_num > num:
        #             return False
        
        # 3rd solution: binary search
        if num == 0 or num == 1:
            return True
        low, high = 1, num
        while low<=high:
            mid = (low+high)//2
            sqr_mid = mid*mid
            if sqr_mid == num:
                return True
            elif sqr_mid < num:
                low = mid+1
            else:
                high = mid-1
        return False
        
            

# @lc code=end

