#
# @lc app=leetcode id=783 lang=python3
#
# [783] Minimum Distance Between BST Nodes
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        # self.mini = float('inf')
        # def findmini(root: TreeNode):
        #     if root is None or root.left is None and root.right is None:
        #         return float('inf')
        #     elif root.left is None:
        #         self.mini = min(self.mini, abs(root.val-root.right.val), findmini(root.right))
        #     elif root.right is None:
        #         self.mini = min(self.mini, abs(root.val-root.left.val), findmini(root.left))
        #     else:
        #         self.mini = min(self.mini, abs(root.val-root.left.val), abs(root.val-root.right.val), \
        #             findmini(root.left), findmini(root.right))
        #     return self.mini
        # findmini(root)
        # return self.mini

        # just traverse:
        self.lst = []
        def inorder(root: TreeNode):
            if root is None:
                return
            inorder(root.left)
            self.lst.append(root.val)
            inorder(root.right)
        inorder(root)
        return min([self.lst[i]-self.lst[i-1] for i in range(1, len(self.lst))])
        
# @lc code=end

