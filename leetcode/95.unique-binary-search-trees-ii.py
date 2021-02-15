#
# @lc app=leetcode id=95 lang=python3
#
# [95] Unique Binary Search Trees II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        # recursion takes a leap of faith
        # return a list of unique tree structs
        def helper(start: int, end: int):
            rtn = []
            if start == end:
                rtn.append(TreeNode(start))
                return rtn
            elif start > end:
                rtn.append(None)
                return rtn
            
            for i in range(start, end+1):
                leftlist = helper(start, i-1)
                rightlist = helper(i+1, end)
                for l in leftlist:
                    for r in rightlist:
                        root = TreeNode(i)
                        root.left = l
                        root.right = r
                        rtn.append(root)
            return rtn
        
        return helper(1, n)
        
# @lc code=end

