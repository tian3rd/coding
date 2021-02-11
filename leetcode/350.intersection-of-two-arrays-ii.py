#
# @lc app=leetcode id=350 lang=python3
#
# [350] Intersection of Two Arrays II
#

# @lc code=start
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # still use set, but keep a dict with count
        dic1 = self.dic_list(nums1)
        dic2 = self.dic_list(nums2)
        rtn = list()
        for ele in set(dic1.keys()).intersection(set(dic2.keys())):
            tally = min(dic1[ele], dic2[ele])
            while tally>0:
                rtn.append(ele)
                tally -= 1
        return rtn 

    def dic_list(self, nums: List[int]) -> Dict:
        if len(nums) == 0:
            return dict()
        rtn = dict()
        for i in range(len(nums)):
            if nums[i] not in rtn.keys():
                rtn[nums[i]] = 1
            else:
                rtn[nums[i]] += 1
        return rtn

        
# @lc code=end

