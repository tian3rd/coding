#
# @lc app=leetcode id=637 lang=python3
#
# [637] Average of Levels in Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if root is None:
            return []
        q1 = deque()
        q2 = deque()
        rtn = list()
        q1.append(root)
        while len(q1)>0 or len(q2)>0:
            node_num = 0
            tal = 0
            while len(q1)>0:
                if q1[0].left is not None:
                    q2.append(q1[0].left)
                if q1[0].right is not None:
                    q2.append(q1[0].right)
                tal += q1.popleft().val
                node_num += 1
            if node_num > 0:
                rtn.append(tal/node_num)
            node_num = 0
            tal = 0
            while len(q2)>0:
                if q2[0].left is not None:
                    q1.append(q2[0].left)
                if q2[0].right is not None:
                    q1.append(q2[0].right)
                tal += q2.popleft().val
                node_num += 1
            if node_num > 0:
                rtn.append(tal/node_num)
        return rtn

# @lc code=end

