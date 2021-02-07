#
# @lc app=leetcode id=219 lang=python3
#
# [219] Contains Duplicate II
#

# @lc code=start
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Time Limit Exceeded
        # for i in range(len(nums)):
        #     for j in range(i+1, i+k+1):
        #         if j >= len(nums):
        #             break
        #         if nums[i] == nums[j]:
        #             return True
        # return False
        
        # if len(nums) <= k + 1: return len(nums) != len(set(nums))
        # if k == 0: return False
        # s = set(nums[:k])
        # for i in range(k, len(nums)):
        #     if nums[i] in s: return True
        #     else:
        #         s.remove(nums[i - k])
        #         s.add(nums[i])
        # return False

        # d = {}
        # for i, n in enumerate(nums):
        #     if n in d and i - d[n] <= k:
        #         return True
        #     d[n] = i
        # return False

        # if k==0:
        #     return False
        # if k>=len(nums):
        #     return len(nums) != len(set(nums))
        # for i in range(len(nums)-k):
        #     s = set(nums[i:i+k+1])
        #     if len(s) != k+1:
        #         return True
        # return False

        dic = dict()
        for i, num in enumerate(nums):
            if num not in dic.keys():
                dic[num] = i
            else:
                if i - dic[num] <= k:
                    return True
                # replace old num index
                dic[num] = i
        return False
# @lc code=end

