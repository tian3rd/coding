#
# @lc app=leetcode id=501 lang=python3
#
# [501] Find Mode in Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        dic = dict()
        self.frequency(root, dic)
        rtn = list()
        maxi = max(dic.values())
        for key in dic:
            if dic[key] == maxi:
                rtn.append(key)
        return rtn
        
    def frequency(self, root: TreeNode, dic: Dict):
        if root is None:
            return
        if root.val not in dic:
            dic[root.val] = 1
        else:
            dic[root.val] += 1
        self.frequency(root.left, dic)
        self.frequency(root.right, dic)
        
# @lc code=end

