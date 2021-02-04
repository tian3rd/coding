#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input array is sorted
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dic = dict()
        for i in range(len(numbers)):
            dic[numbers[i]] = []
        for i in range(len(numbers)):
            dic[numbers[i]].append(i)
        for i in range(len(numbers)):
            if target-numbers[i] in dic.keys():
                if len(dic[target-numbers[i]]) > 1:
                    return [dic[numbers[i]][0]+1, dic[numbers[i]][1]+1]
                else:
                    return [dic[numbers[i]][0]+1, dic[target-numbers[i]][0]+1]
        
# @lc code=end

