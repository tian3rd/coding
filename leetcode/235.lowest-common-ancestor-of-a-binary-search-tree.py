#
# @lc app=leetcode id=235 lang=python3
#
# [235] Lowest Common Ancestor of a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:
            return None
        # case 1: if p contains q or q contains p
        if self.contains_node(p, q):
            return p
        if self.contains_node(q, p):
            return q
        # case 2: recursively find out the lca
        if self.contains_node(root, p) and self.contains_node(root, q):
            if (self.contains_node(root.left, p) and self.contains_node(root.right, q)) \
                or (self.contains_node(root.right, p) and self.contains_node(root.left, q)):
                return root
            elif self.contains_node(root.left, p) and self.contains_node(root.left, q):
                return self.lowestCommonAncestor(root.left, p, q)
            else:
                return self.lowestCommonAncestor(root.right, p, q)

    # helper func to check if node exists in root
    def contains_node(self, root: 'TreeNode', node: 'TreeNode') -> bool:
        if root is None:
            return False
        if root == node:
            return True
        return self.contains_node(root.left, node) or self.contains_node(root.right, node)
        
    
    # NOTE: this is a bst, so take advantage of the ordered val!!
# @lc code=end

