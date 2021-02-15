#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        self.rtn = []
        def helper(root: TreeNode):
            if root is None:
                return
            helper(root.left)
            self.rtn.append(root.val)
            helper(root.right)
        helper(root)
        return self.rtn
        
# @lc code=end

