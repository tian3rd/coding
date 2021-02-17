#
# @lc app=leetcode id=653 lang=python3
#
# [653] Two Sum IV - Input is a BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        if root is None or (root.left is None and root.right is None):
            return False
        # inorder traversal
        # def inorder(root: TreeNode) -> list:
        #     if root is None:
        #         return []
        #     rtn = []
        #     rtn += inorder(root.left)
        #     rtn.append(root.val)
        #     rtn += inorder(root.right)
        #     return rtn
        # lst = inorder(root)
        # left, right = 0, len(lst)-1
        # while left < right:
        #     if lst[left]+lst[right] == k:
        #         return True
        #     if lst[left]+lst[right] < k:
        #         left += 1
        #     else:
        #         right -= 1
        # return False

        # recursive 
        self.setnum = set()
        def find(root: TreeNode, k: int) -> bool:
            if root is None: 
                return False
            if find(root.left, k):
                return True
            # remember past nodes' vals
            if k-root.val in self.setnum:
                return True
            self.setnum.add(root.val)
            if find(root.right, k):
                return True
        return find(root, k)
            
# @lc code=end

