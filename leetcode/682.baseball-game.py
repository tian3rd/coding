#
# @lc app=leetcode id=682 lang=python3
#
# [682] Baseball Game
#

# @lc code=start
class Solution:
    def calPoints(self, ops: List[str]) -> int:
        points = []
        for op in ops:
            if op.isnumeric() or len(op)>=2:
                points.append(int(op))
            if op == "C":
                points.pop()
            if op == "D":
                points.append(points[-1]*2)
            if op == "+":
                points.append(points[-1]+points[-2])
        # print(points)
        return sum(points)

        
# @lc code=end

