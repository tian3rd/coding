#
# @lc app=leetcode id=257 lang=python3
#
# [257] Binary Tree Paths
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        # using dfs 
        s0 = ""
        rtn = []
        self.dfs(root, rtn, s0)
        return rtn

    def dfs(self, root: TreeNode, rtn: List[str], s: str):
        if root is None:
            return
        s += "->"+str(root.val)
        if root.left is None and root.right is None:
            rtn.append(s[2:])
            return
        if root.left is not None:
            self.dfs(root.left, rtn, s)
        if root.right is not None:
            self.dfs(root.right, rtn, s)

        
# @lc code=end

