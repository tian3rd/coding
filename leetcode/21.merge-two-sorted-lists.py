#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # use two head, one remembers first pos, second traverses
        dummyHead = rtn = ListNode(val=-101, next=None)
        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                rtn.next = l1
                l1 = l1.next
            else:
                rtn.next = l2
                l2 = l2.next
            rtn = rtn.next
        if l1 is None:
            rtn.next = l2
        if l2 is None:
            rtn.next = l1
        return dummyHead.next


        
# @lc code=end

