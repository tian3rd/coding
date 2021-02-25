#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#

# @lc code=start
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # this problem is not well organized, should be better if [a, b] doesn't include
        # b so that [1, 1] doesn't exist. Or maybe my code is too ...
        if len(intervals) == 0:
            return [newInterval]
        state = [False for _ in range(max(intervals[-1][1], newInterval[1])+1)]
        for ele in intervals:
            if ele[0] == ele[1]:
                state[ele[0]] = -1
            for i in range(ele[0], ele[1]):
                state[i] = True
        for i in range(newInterval[0], newInterval[1]):
            state[i] = True
        if state[newInterval[1]] == -1:
            state[newInterval[1]] = False       
        if newInterval[0] == newInterval[1] and state[newInterval[0]] == False and state[newInterval[0]-1] == False:
            state[newInterval[0]] = -1

        initial = 0
        rtn = []
        print(state)
        while initial < len(state):
            while initial < len(state) and state[initial] == -1:
                rtn.append([initial, initial])
                initial += 1 
            while initial < len(state) and state[initial] == False:
                initial += 1
            first = initial
            while initial < len(state) and state[initial] == True:
                initial += 1
            if first != initial:
                rtn.append([first, initial])
        return rtn
        
# @lc code=end

