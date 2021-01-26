#
# @lc app=leetcode id=100 lang=python3
#
# [100] Same Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None:
            return q is None
        elif q is None:
            return p is None
        elif p.left is None and p.right is None and q.right is None and q.left is None:
            return p.val == q.val
        elif p.left is None and p.right is not None:
            return q.left is None and p.val == q.val and self.isSameTree(p.right, q.right)
        elif p.right is None and p.left is not None:
            return q.right is None and p.val == q.val and self.isSameTree(p.left, q.left)
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
# @lc code=end

