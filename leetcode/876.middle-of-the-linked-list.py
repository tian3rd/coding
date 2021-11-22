#
# @lc app=leetcode id=876 lang=python3
#
# [876] Middle of the Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # two pointers, one slow 1x and one fast 2x
        dummy_head = ListNode(0)
        dummy_head.next = head
        slow = dummy_head
        fast = dummy_head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow.next
        
# @lc code=end

