#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        # sliding window
        left, right, rtn = 0, 0, 0
        dic = {s[i]: 0 for i in range(len(s))}
        while right < len(s):
            # update/add right char in dict
            c = s[right]
            dic[c] += 1
            right += 1
            # if the added char is repeated, then delete all chars before it (including the char itself) to make it unique
            while dic[c] > 1:
                d = s[left]
                dic[d] -= 1
                left += 1
            rtn = max(rtn, right - left)
        return rtn


        
# @lc code=end

