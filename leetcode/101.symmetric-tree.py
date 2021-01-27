#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # use recursion
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None or (root.left is None and root.right is None):
            return True
        if (root.left is None and root.right is not None) or \
            (root.left is not None and root.right is None):
            return False
        return root.left.val == root.right.val and \
            self.isSymmySsi(root.left, root.right)

    # use helper func to determine the symmetry
    def isSymmySsi(self, node1, node2) -> bool:
        if node1 is None and node2 is None:
            return True
        if (node1 is None and node2 is not None) or \
            (node2 is None and node1 is not None):
            return False
        if node1.val != node2.val:
            return False
        return self.isSymmySsi(node1.left, node2.right) and \
            self.isSymmySsi(node1.right, node2.left)
        
# @lc code=end

