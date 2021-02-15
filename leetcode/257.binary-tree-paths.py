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
    #     # using dfs 
    #     s0 = ""
    #     rtn = []
    #     self.dfs(root, rtn, s0)
    #     return rtn

    # def dfs(self, root: TreeNode, rtn: List[str], s: str):
    #     if root is None:
    #         return
    #     s += "->"+str(root.val)
    #     if root.left is None and root.right is None:
    #         rtn.append(s[2:])
    #         return
    #     if root.left is not None:
    #         self.dfs(root.left, rtn, s)
    #     if root.right is not None:
    #         self.dfs(root.right, rtn, s)

        self.s = ""
        self.rtn = []
        def helper(root: TreeNode):
            if root is None:
                return
            self.s += "->"+str(root.val)
            # if it's a leaf
            if root.left is None and root.right is None:
                self.rtn.append(self.s[2:])
            if root.left is not None:
                # use a temporary s0 to remember original string
                s0 = self.s
                helper(root.left)
                # set it to original for the right helper
                self.s = s0
            if root.right is not None:
                helper(root.right)
        
        helper(root)
        return self.rtn
        
# @lc code=end

