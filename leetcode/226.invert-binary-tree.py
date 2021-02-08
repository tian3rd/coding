#
# @lc app=leetcode id=226 lang=python3
#
# [226] Invert Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None
        elif root.left is None and root.right is None:
            return root
        elif root.left is not None and root.right is None:
            root.right = self.invertTree(root.left)
            root.left = None
        elif root.left is None and root.right is not None:
            root.left = self.invertTree(root.right)
            root.right = None
        else:
            temp = self.invertTree(root.left)
            root.left = self.invertTree(root.right)
            root.right = temp
        return root
        
# @lc code=end

