#
# @lc app=leetcode id=107 lang=python3
#
# [107] Binary Tree Level Order Traversal II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # recursion
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        elif root.left is None and root.right is None:
            return [[root.val]]
        elif root.left is not None and root.right is None:
            l = self.levelOrderBottom(root.left)
            l.append([root.val])
            return l
        elif root.left is None and root.right is not None:
            r = self.levelOrderBottom(root.right)
            r.append([root.val])
            return r
        else:
            l = self.levelOrderBottom(root.left)
            r = self.levelOrderBottom(root.right)
            if len(l) >= len(r):
                for i in range(len(r)):
                    l[len(l)-1-i] += r[len(r)-1-i]
                l.append([root.val])
                return l
            else:
                for i in range((len(l))):
                    l[len(l)-1-i] += r[len(r)-1-i]
                l = r[:(len(r)-len(l))] + l
                l.append([root.val])
                return l
    
    # forward appending
    # def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        
# @lc code=end

