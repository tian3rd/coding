#
# @lc app=leetcode id=404 lang=python3
#
# [404] Sum of Left Leaves
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if root is None or (root.left is None and root.right is None):
            return 0
        if root.left is not None:
            if root.left.left is None and root.left.right is None:
                return root.left.val+self.sumOfLeftLeaves(root.right)
            else:
                return self.sumOfLeftLeaves(root.left)+self.sumOfLeftLeaves(root.right)
        if root.left is None and root.right is not None:
            return self.sumOfLeftLeaves(root.right)
# @lc code=end

