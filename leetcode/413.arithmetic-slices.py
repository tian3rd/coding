#
# @lc app=leetcode id=413 lang=python3
#
# [413] Arithmetic Slices
#

# @lc code=start
class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        if len(A)<3:
            return 0
        slist = []
        i = 1
        while i <= len(A)-2:
            if A[i-1]-A[i] == A[i]-A[i+1]:
                # first of long slice
                slist.append(i-1)
                diff = A[i-1]-A[i]
                while i+1<=len(A)-1 and A[i]-A[i+1]==diff:
                    i += 1
                # last of slice
                slist.append(i)
                i += 1
            else:
                i += 1
        if len(slist)==0:
            return 0
        else:
            rtn = 0
            for i in range(0, len(slist), 2):
                rtn += (slist[i+1]-slist[i])*(slist[i+1]-slist[i]-1)//2
        return rtn

# @lc code=end

