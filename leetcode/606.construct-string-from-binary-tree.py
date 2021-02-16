#
# @lc app=leetcode id=606 lang=python3
#
# [606] Construct String from Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, t: TreeNode) -> str:
        def preorder(root: TreeNode) -> str:
            if root is None:
                return ""
            if root.left is None and root.right is None:
                return str(root.val)
            rtn = ""
            rtn += str(root.val)
            rtn += "("+preorder(root.left)+")"
            # omit the "()" if there is no right node
            if root.right is not None:
                rtn += "("+preorder(root.right)+")"
            return rtn
        rtn = preorder(t)
        return rtn
        
# @lc code=end

