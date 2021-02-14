#
# @lc app=leetcode id=496 lang=python3
#
# [496] Next Greater Element I
#

# @lc code=start
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic = {key:-1 for key in nums2}
        for i in range(len(nums2)-2, -1, -1):
            if nums2[i] < nums2[i+1]:
                dic[nums2[i]] = nums2[i+1]
            else:
                temp = nums2[i+1]
                while nums2[i] > temp:
                    # if temp == nums2[-1]:
                    #     temp = dic[temp]
                    #     break
                    if temp == -1:
                        break
                    temp = dic[temp]
                dic[nums2[i]] = temp
        rtn = list()
        for i in range(len(nums1)):
            rtn.append(dic[nums1[i]])
        return rtn
        
# @lc code=end

