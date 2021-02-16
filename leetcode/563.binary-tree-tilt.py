#
# @lc app=leetcode id=563 lang=python3
#
# [563] Binary Tree Tilt
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: TreeNode) -> int:
        # if root is None or root.left is None and root.right is None:
        #     return 0
        # if root.left is None:
        #     return abs(root.right.val)
        # if root.right is None:
        #     return abs(root.left.val)
        # return abs(root.left.val-root.right.val)+self.findTilt(root.left)+self.findTilt(root.right)

        self.rtn = 0
        def sum_nodes(root: TreeNode) -> int:
            if root is None:
                return 0
            if root.left is None and root.right is None:
                return root.val
            return root.val+sum_nodes(root.left)+sum_nodes(root.right)

        def inorder(root: TreeNode) -> int:
            if root is None:
                return
            inorder(root.left)
            self.rtn += abs(sum_nodes(root.left)-sum_nodes(root.right))
            inorder(root.right)
        
        inorder(root)
        return self.rtn
        


# @lc code=end

