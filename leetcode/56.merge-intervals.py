#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals
        # first sort
        intervals = sorted(intervals)
        # track the left and right index of not interleaved value
        first, second = 0, 1
        rtn, lst = [], []
        for ele in intervals:
            lst.append(ele[0])
            lst.append(ele[1])
        n = len(lst)
        while first <= n-2:
            right = lst[second]
            # if second is larger than next, or the max right value is larger than next
            # there must have been overlapping
            while second +2 <= n-1 and (lst[second] >= lst[second+1] \
                or right >= lst[second+1]):
                # remember the largest right scope
                right = max(right, lst[second+2])
                second += 2
            rtn.append([lst[first], right])
            # move pointer to next
            first = second+1
            second += 2
        return rtn

# @lc code=end

