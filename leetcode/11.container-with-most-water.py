#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # left = 0
        # right = len(height)-1
        # max_area = (right-left)*min(height[left], height[right])
        # if len(height) == 2:
        #     return max_area
        # i = 2
        # while i <= len(height):
        #     for l in range(left+1, right):
        #         i += 1
        #         if height[l] > height[left]:
        #             max_area = max(max_area, (right-l)*min(height[l], height[right]))
        #             left = l
        #             if height[left] > height[right]:
        #                 break
            
        #     for r in range(right, left, -1):
        #         i += 1
        #         if height[r] > height[right]:
        #             max_area = max(max_area, (r-left)*min(height[left], height[r]))
        #             right = r
        #             if height[right] > height[left]:
        #                 break
        #     # break
        
        # return max_area

        left, right = 0, len(height)-1
        max_area = 0
        while left < right:
            max_area = max(max_area, (right- left)*min(height[left], height[right]))
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return max_area
            
# @lc code=end

