#
# @lc app=leetcode id=116 lang=python3
#
# [116] Populating Next Right Pointers in Each Node
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        q = []
        q.append(root)
        while q:
            sz = len(q)
            for i in range(sz):
                cur = q.pop(0)
                if i < sz - 1:
                    cur.next = q[0]
                # the leaf nodes don't need to add their null children
                if cur.left and cur.right:
                    q.append(cur.left)
                    q.append(cur.right)
        return root
        
# @lc code=end

