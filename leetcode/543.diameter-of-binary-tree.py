#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
    #     if root is None or (root.left is None and root.right is None):
    #         return 0
    #     paths = self.inorder(root)
    #     return max(paths)

    # def inorder(self, root: TreeNode) -> List[int]:
    #     rtn = []
    #     if root:
    #         rtn = self.inorder(root.left)
    #         rtn.append(self.longest(root.left)+self.longest(root.right))
    #         rtn += self.inorder(root.right)
    #     return rtn

    # def longest(self, root: TreeNode) -> int:
    #     if root is None:
    #         return 0
    #     if root.left is None and root.right is None:
    #         return 1
    #     if root.left is None:
    #         return 1+self.longest(root.right)
    #     if root.right is None:
    #         return 1+self.longest(root.left)
    #     return 1+max(self.longest(root.left), self.longest(root.right))

        self.d = 0

        # return the longest no. of nodes from left or righ(including root)
        def helper(root: TreeNode) -> int:
            if root is None:
                return 0
            left, right = helper(root.left), helper(root.right)
            # for every recursion, get the max of path for depth
            self.d = max(self.d, left+right)
            return 1+max(left, right)
        
        helper(root)
        return self.d
        
# @lc code=end

