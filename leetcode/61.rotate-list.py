#
# @lc app=leetcode id=61 lang=python3
#
# [61] Rotate List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head is None:
            return head
        ptr1 = head
        n = 1
        while ptr1.next:
            n += 1
            ptr1 = ptr1.next
        # ptr1 now points to the last node
        if k % n == 0:
            return head
        # k means to shift left, then n- means to shift right
        k = n - k % n
        # ptr2 points to the head of returned list, ptr3 add the traversed nodes
        ptr2, ptr3 = head, head
        while k != 0:
            k -= 1
            ptr2 = ptr2.next
            ptr1.next = ListNode(ptr3.val)
            ptr1 = ptr1.next
            ptr3 = ptr3.next
        return ptr2
# @lc code=end

