class Solution:
    def longestPalindrome(self, word1: str, word2: str) -> int:
        # m, n = len(word1), len(word2)
        # dp = [[0]*(n+1) for _ in range(m+1)]
        # word3 = word2[::-1]
        # for i in range(m):
        #     for j in range(n):
        #         if word1[i] == word3[j]:
        #             dp[i+1][j+1] = dp[i][j] + 1
        #         else:
        #             dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])
        # if dp[m][n] == dp[m][n-1] or dp[m][n] == dp[m-1][n]:
        #     return 2*dp[m][n]+1
        # return 2*dp[m][n]

        words = word1+word2
        