#
# @lc app=leetcode id=671 lang=python3
#
# [671] Second Minimum Node In a Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        self.mini = root.val
        def findlarger(root:TreeNode) -> int:
            if root is None:
                return -1
            if root.val > self.mini:
                return root.val
            lf, rf = findlarger(root.left), findlarger(root.right)
            if lf*rf < 0:
                return max(lf, rf)
            if lf>0 and rf>0:
                return min(lf, rf)
            return -1
        return findlarger(root)
# @lc code=end

