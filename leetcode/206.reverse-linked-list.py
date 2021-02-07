#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None: 
            return head
        first, second = head, head.next
        # prevent loop of the first node
        first.next = None
        while second is not None:
            temp = second.next
            second.next = first
            first = second
            second = temp
        return first
        
# @lc code=end

