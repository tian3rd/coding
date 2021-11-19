#
# @lc app=leetcode id=111 lang=python3
#
# [111] Minimum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        # 
        # if root is None:
        #     return 0
        # if root.left is None and root.right is None:
        #     return 1
        # if root.left is not None and root.right is None:
        #     return 1+self.minDepth(root.left)
        # if root.left is None and root.right is not None:
        #     return 1+self.minDepth(root.right)
        # return 1+min(self.minDepth(root.left), self.minDepth(root.right))

        # using BFS
        if root is None:
            return 0
        # using list as a simple queue
        q = [root]
        # already has root, so depth rtn is 1
        rtn = 1
        while q:
            sz = len(q)
            for _ in range(sz):
                # get the first out of the queue
                cur = q.pop(0)
                # tell if we get to the target leaf
                if cur.left is None and cur.right is None:
                    return rtn
                # if not, keep to the next level
                if cur.left is not None:
                    q.append(cur.left)
                if cur.right is not None:
                    q.append(cur.right)
            # after each for loop of the same depth level, we go deeper
            rtn += 1
        return rtn
        
# @lc code=end

