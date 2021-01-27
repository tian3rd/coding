#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        return self.depth(root)

    def depth(self, node) -> int:
        if node is None:
            return 0
        if node.left is None and node.right is None:
            return 1
        if node.left is None and node.right is not None:
            return 1+self.depth(node.right)
        if node.right is None and node.left is not None:
            return 1+self.depth(node.left)
        if node.left is not None and node.right is not None:
            return 1+max(self.depth(node.left), self.depth(node.right))
        
# @lc code=end

