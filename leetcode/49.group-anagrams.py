#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        rtn = dict()
        for element in strs:
            temp = ''.join(sorted(element))
            if temp not in rtn:
                rtn[temp] = [element]
            else:
                rtn[temp].append(element)
        return [rtn[key] for key in rtn.keys()]
        
# @lc code=end

