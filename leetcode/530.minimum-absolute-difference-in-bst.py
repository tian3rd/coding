#
# @lc app=leetcode id=530 lang=python3
#
# [530] Minimum Absolute Difference in BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def getMinimumDifference(self, root: TreeNode) -> int:
    #     # key is to find the precessor and successor nodes of root
    #     diffs = self.inorder(root)
    #     return min(diffs)
    
    # def inorder(self, root: TreeNode) -> List[int]:
    #     rtn = []
    #     if root and (root.left or root.right):
    #         rtn = self.inorder(root.left)
    #         rtn.append(self.mindiff(root))
    #         rtn += self.inorder(root.right)
    #     return rtn
                
    # def mindiff(self, root: TreeNode) -> int:
    #     if self.precessor(root) is None:
    #         return self.successor(root).val-root.val
    #     elif self.successor(root) is None:
    #         return root.val-self.precessor(root).val
    #     return min(self.successor(root).val-root.val, root.val-self.precessor(root).val)
            
    # def precessor(self, root: TreeNode) -> TreeNode:
    #     if root is None:
    #         return None
    #     if root.left is None:
    #         return None
    #     root = root.left
    #     while root.right is not None:
    #         root = root.right
    #     return root
    
    # def successor(self, root: TreeNode) -> TreeNode:
    #     if root is None: 
    #         return None
    #     if root.right is None:
    #         return None
    #     root = root.right
    #     while root.left is not None:
    #         root = root.left
    #     return root

    def getMinimumDifference(self, root: TreeNode) -> int: 
        # first convert to a list of node vals, ascended
        self.lst = []      
        def inorder(root: TreeNode):
            if root is None:
                return
            inorder(root.left)
            self.lst.append(root.val)
            inorder(root.right)
        inorder(root)

        # second, traverse and find the smallest
        mini = self.lst[1]-self.lst[0]
        for i in range(len(self.lst)-1):
            mini = min(mini, self.lst[i+1]-self.lst[i])
        return mini
        
# @lc code=end

