#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # multiple binary searches to get to largest and smallest index
        def bisearch(nums: List[int], target: int) -> int:
            low, high = 0, len(nums)-1
            while low<=high:
                # print(low, high)
                mid = (low+high)//2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    low = mid+1
                else:
                    high = mid-1
            return -1
        if bisearch(nums, target) == -1:
            return [-1, -1]
        i0 = bisearch(nums, target)
        i1 = i0-1
        i2 = i0+1
        while i1 >= 0 and bisearch(nums[:i1+1], target) != -1:
            i1 = bisearch(nums[:i1+1], target)-1
        while i2 <= len(nums)-1 and bisearch(nums[i2:], target) != -1:
            # need to increment 'cause starting from i2ui
            i2 += bisearch(nums[i2:], target)+1
        return [i1+1, i2-1]

        
# @lc code=end

