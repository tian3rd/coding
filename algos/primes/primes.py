import unittest

class EratosthenesSievePrimes:
    def __init__(self, n: int) -> None:
        '''
        eratosthenes sieve: https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes ;
        n: the upper bound of the prime list you wanna generate
        '''
        self.n = n

    def generate(self) -> list:
        '''
        generate the prime list up till n.
        '''
        if self.n < 2:
            return []
        isprime = [False, False] + [True for _ in range(1,self.n)]
        for i in range(2, self.n+1):
            if isprime[i]:
                for j in range(i*i, self.n+1, i):
                    isprime[j] = False
        rtn = []
        for i in range(self.n+1):
            if isprime[i]:
                rtn.append(i)
        return rtn

class TestPrimes(unittest.TestCase):
    def test_primes(self):
        """
        List of primes: https://en.wikipedia.org/wiki/List_of_prime_numbers
        """
        primes1 = EratosthenesSievePrimes(30)
        self.assertEqual(primes1.generate(), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29])
        primes2 = EratosthenesSievePrimes(1000)
        self.assertEqual(primes2.generate(), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997])


if __name__ == '__main__':
    unittest.main()

