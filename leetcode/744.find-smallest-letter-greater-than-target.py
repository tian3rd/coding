#
# @lc app=leetcode id=744 lang=python3
#
# [744] Find Smallest Letter Greater Than Target
#

# @lc code=start
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        # first delete the duplicates
        lettersset = set()
        lettersuni = []
        for l in letters:
            if l not in lettersset:
                lettersset.add(l)
                lettersuni.append(l)

        # then binary search
        def bs():
            low, high = 0, len(lettersuni)-1
            while low<=high:
                mid = (low+high)//2
                if lettersuni[mid] == target:
                    return mid+1
                elif lettersuni[mid] < target:
                    low = mid+1
                else:
                    high = mid-1
            if low>high:
                return low
        
        rtn = bs()
        if rtn == len(lettersuni):
            return lettersuni[0]
        return lettersuni[rtn]

        
# @lc code=end

