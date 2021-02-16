#
# @lc app=leetcode id=605 lang=python3
#
# [605] Can Place Flowers
#

# @lc code=start
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        spots = len(flowerbed)
        flowerbed = [0]+flowerbed+[0]
        maxi = 0
        for i in range(1, spots+1):
            if flowerbed[i-1]+flowerbed[i+1]==0 and flowerbed[i]==0:
                maxi += 1
                flowerbed[i] = 1
        return maxi>=n

        
# @lc code=end

