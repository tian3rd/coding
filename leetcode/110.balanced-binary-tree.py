#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def isBalanced(self, root: TreeNode) -> bool:
    #     if root is None:
    #         return True
    #     node_num = self.count_nodes(root)
    #     node_depth = self.max_depth(root)
    #     if 2**(node_depth-1) <= node_num and node_num < 2**node_depth:
    #         return True
    #     return False
        
    # def count_nodes(self, root: TreeNode) -> int:
    #     if root is None:
    #         return 0
    #     if root.left is None and root.right is None:
    #         return 1
    #     if root.left is not None and root.right is None:
    #         return 1+self.count_nodes(root.left)
    #     if root.left is None and root.right is not None:
    #         return 1+self.count_nodes(root.right)
    #     return 1+self.count_nodes(root.left)+self.count_nodes(root.right)
    
    def max_depth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        if root.left is not None and root.right is None:
            return 1+self.max_depth(root.left)
        if root.left is None and root.right is not None:
            return 1+self.max_depth(root.right)
        return 1+max(self.max_depth(root.left), self.max_depth(root.right))

    def isBalanced(self, root: TreeNode) -> bool:
        if root is None:
            return True
        if root.left is None and root.right is not None:
            return self.max_depth(root.right) == 1
        if root.left is not None and root.right is None:
            return self.max_depth(root.left) == 1
        return abs(self.max_depth(root.left)-self.max_depth(root.right))<=1 \
            and self.isBalanced(root.left) and self.isBalanced(root.right)

# @lc code=end

