#
# @lc app=leetcode id=108 lang=python3
#
# [108] Convert Sorted Array to Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if nums is None:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0])
        # if len(nums) == 2:
        #     node = TreeNode(nums[1])
        #     node.left = TreeNode(nums[0])
        #     return node
        # if len(nums) == 3:
        #     node = TreeNode(nums[1])
        #     node.left = TreeNode(nums[0])
        #     node.right = TreeNode(nums[2])
        #     return node
        if len(nums) > 1:
            node = TreeNode(nums[len(nums)//2])
            node.left = self.sortedArrayToBST(nums[:len(nums)//2])
            node.right = self.sortedArrayToBST(nums[len(nums)//2+1:])
            return node

# @lc code=end

