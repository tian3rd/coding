#
# @lc app=leetcode id=866 lang=python3
#
# [866] Prime Palindrome
#

# @lc code=start
class Solution:
    def primePalindrome(self, n: int) -> int:
        if n == 1 or n == 2:
            return 2
        def is_palindrome(n):
            return str(n) == str(n)[::-1]
        def is_prime(n):
            if n <= 3:
                return n > 1
            if n % 2 == 0 or n % 3 == 0:
                return False
            i = 5
            while i ** 2 <= n:
                if n % i == 0 or n % (i + 2) == 0:
                    return False
                i += 6
            return True

        while True:
            # observation that if a palindrome integer greater than 11 with even number of digits can be divided by 11 (so not a prime), so we skip all even digits numbers
            if len(str(n)) % 2 == 0 and n > 11:
                # starting from 10...01 (odd number of 0s)
                n = int('1' + '0' * (len(str(n)) - 1) + '1')
                continue
            if is_palindrome(n) and is_prime(n):
                return n
            n += 1
        
# @lc code=end

