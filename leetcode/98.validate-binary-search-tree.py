#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # convert it to an ordered list using inorder traversal
        if root.left is None and root.right is None:
            return True
        self.lst = list()

        def inorder(root: TreeNode):
            if root is None:
                return
            inorder(root.left)
            self.lst.append(root.val)
            inorder(root.right)
        
        inorder(root)
        for i in range(len(self.lst)-1):
            if self.lst[i]>=self.lst[i+1]:
                return False
        return True
        
# @lc code=end

