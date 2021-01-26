#
# @lc app=leetcode id=83 lang=python3
#
# [83] Remove Duplicates from Sorted List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummyHead = pointer = ListNode()
        # while loop exit when head points to None
        while head is not None:
            # while loop exits when head has no next or is not equal to next val
            while head.next is not None and head.val == head.next.val:
                head = head.next
            pointer.next = head
            pointer = pointer.next
            head = head.next
        return dummyHead.next
        
# @lc code=end

