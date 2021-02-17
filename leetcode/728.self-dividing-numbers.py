#
# @lc app=leetcode id=728 lang=python3
#
# [728] Self Dividing Numbers
#

# @lc code=start
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        rtn = []
        for n in range(left, right+1):
            nlist = str(n)
            nset = set([int(_) for _ in nlist])
            if 0 in nset:
                continue
            issdn = True
            for num in nset:
                if n%num != 0:
                    issdn = False
            if issdn:
                rtn.append(n)
        return rtn
        
# @lc code=end

