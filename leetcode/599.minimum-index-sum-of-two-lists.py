#
# @lc app=leetcode id=599 lang=python3
#
# [599] Minimum Index Sum of Two Lists
#

# @lc code=start
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        mini = len(list1)+len(list2)
        dic2 = {list2[i]:i for i in range(len(list2))}
        set2 = set(list2)
        # rtn = []
        for i in range(len(list1)):
            if  list1[i] in set2:
                if dic2[list1[i]]+i<mini:
                    mini = i+dic2[list1[i]]
                    rtn = []
                if dic2[list1[i]]+i==mini:
                    rtn.append(list1[i])
        return rtn
        
# @lc code=end

