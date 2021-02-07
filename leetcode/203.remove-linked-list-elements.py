#
# @lc app=leetcode id=203 lang=python3
#
# [203] Remove Linked List Elements
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummyHead = pointer = ListNode()
        dummyHead.next = pointer.next = head
        while pointer is not None:
            if pointer.next is None:
                break
            while pointer.next is not None and pointer.next.val == val:
                pointer.next = pointer.next.next
            pointer = pointer.next
        return dummyHead.next
        
# @lc code=end

