#
# @lc app=leetcode id=1358 lang=python3
#
# [1358] Number of Substrings Containing All Three Characters
#

# @lc code=start
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        # if len(s) < 3:
        #     return 0
        # rtn = 0
        # head = tail = 0
        # dic = {"a": 0, "b": 0, "c": 0}
        # while head < len(s)-2:
        #     while tail < len(s):
        #         dic[s[tail]] += 1
        #         if dic["a"]*dic["b"]*dic["c"] != 0:
        #             break
        #         tail += 1
        #     if tail <= len(s)-1:
        #         rtn += len(s)-tail
        #     # if tail == len(s)-1:
        #     #     if dic["a"]*dic["b"]*dic["c"] != 0:
        #     #         rtn += 1
        #     while head + 2 <= tail:
        #         dic[s[head]] -= 1
        #         head += 1
        #         if dic["a"]*dic["b"]*dic["c"] != 0:
        #             rtn += len(s)-tail
        #     tail += 1
        # return rtn

        if len(s) < 3: 
            return 0
        dic = {"a": -1, "b": -1, "c": -1}
        rtn = 0
        for i, ch in enumerate(s):
            # record the last appearance of ch
            dic[ch] = i
            # if a, b, c all appear, then there're min(apperance pos)+1 up till now for valid strings
            rtn += min(dic.values())+1
        return rtn
        
# @lc code=end

