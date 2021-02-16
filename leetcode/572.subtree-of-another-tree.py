#
# @lc app=leetcode id=572 lang=python3
#
# [572] Subtree of Another Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:

        def preorder(root: TreeNode) -> str:
            if root is None:
                return "null"
            s = ""
            s = "#"+str(root.val)+"#"
            if root.left is None:
                s += "lnone"
            else:
                s += "l"+preorder(root.left)+"l"
            if root.right is None:
                s += "rnone"
            else:
                s += "r"+preorder(root.right)+"r"
            return s
        
        s1 = preorder(s)
        s2 = preorder(t)
        if s2 not in s1:
            return False
        return True

        
# @lc code=end

