#
# @lc app=leetcode id=278 lang=python3
#
# [278] First Bad Version
#

# @lc code=start
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        # binary search 
        left, right = 1, n
        while left <= right:
            if isBadVersion((left+right)//2) is False:
                left = (left+right)//2 + 1
            else:
                right = (left+right)//2 - 1
        return left
        
# @lc code=end

