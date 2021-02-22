#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dumbhead = ListNode()
        dumbhead.next = head
        prev, first = dumbhead, head
        if first is None or first.next is None:
            return head
        second = first.next
        while first is not None and second is not None:
            # swap first and second, and link prev to new node
            temp = second.next
            second.next = first
            first.next = temp
            prev.next = second
            
            prev, first = first, temp
            
            if first is None:
                break
            second = first.next
        
        return dumbhead.next
        
# @lc code=end

