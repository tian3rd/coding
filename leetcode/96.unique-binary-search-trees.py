#
# @lc app=leetcode id=96 lang=python3
#
# [96] Unique Binary Search Trees
#

# @lc code=start
class Solution:
    def numTrees(self, n: int) -> int:
        # still recursion, believe...
        # def helper(start: int, end: int) -> int:
        #     if start>end:
        #         return 0
        #     if start==end:
        #         return 1
        #     rtn = 0
        #     for i in range(start, end+1):
        #         if i == start:
        #             rtn += helper(i+1, end)
        #         elif i == end:
        #             rtn += helper(start, i-1)
        #         else:
        #             rtn += helper(start, i-1)*helper(i+1, end)
        #     return rtn
        # return helper(1, n)
        
        # self.cnt = [1,2]
        # def helper(n: int):
        #     if n<2:
        #         return n+1
        #     tal = 0
        #     for i in range(n+1):
        #         if i == 0:
        #             tal += helper(n-1)
        #         if i == n:
        #             tal += helper(n-1)
        #         else:
        #             tal += helper(i-1)*helper(n-(i+1))
        #     self.cnt.append(tal)
        #     return tal
        # return helper(n-1)

        # refer to https://www.geeksforgeeks.org/number-of-unique-bst-with-a-given-key-dynamic-programming/
        rtn = [0]*(n+1)
        rtn[0], rtn[1] = 1, 1
        if n == 1:
            return rtn[n]
        # calculate the rest i-th one by one accumulatively
        # use j as a separator, left has j-1 unique, right has i-j unique
        for i in range(2, n+1):
            for j in range(1, i+1):
                rtn[i] += rtn[j-1]*rtn[i-j]
        
        return rtn[n]

# @lc code=end

