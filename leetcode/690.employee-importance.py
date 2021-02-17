#
# @lc app=leetcode id=690 lang=python3
#
# [690] Employee Importance
#

# @lc code=start
"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""
from collections import deque
class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        importance = dict()
        subs = dict()
        for worker in employees:
            importance[worker.id] = worker.importance
            subs[worker.id] = worker.subordinates
        # use a queue
        q = deque()
        q.append(id)
        rtn = 0
        while q:
            who = q.popleft()
            rtn += importance[who]
            for sub in subs[who]:
                q.append(sub)
        return rtn

        
# @lc code=end

