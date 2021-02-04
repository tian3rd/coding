#
# @lc app=leetcode id=160 lang=python3
#
# [160] Intersection of Two Linked Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA is None or headB is None:
            return None
        # make two ll the same length, then traverse to see if they point to the same node
        hA, hB = headA, headB
        lenA, lenB = 0, 0
        while hA is not None:
            lenA += 1
            hA = hA.next
        while hB is not None:
            lenB += 1
            hB = hB.next
        if lenA > lenB:
            for _ in range(lenA-lenB):
                headA = headA.next
        else:
            for _ in range(lenB-lenA):
                headB = headB.next
        while headA is not None:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        return None

# @lc code=end

