#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # if head.next is None:
        #     return None
        # dummyHead = ListNode()
        # dummyHead.next = h = head
        # l = 0
        # while h is not None:
        #     l += 1
        #     h = h.next
        # removed = l - n
        # if removed == 0:
        #     return head.next
        # for i in range(l):
        #     if i+1 == removed:
        #         head.next = head.next.next
        #         return dummyHead.next
        #     head = head.next
        
        # # using two pointers to keep track of positions
        # # first: has two parts, n and length-n;
        # # second: has two parts, length-n, n;
        # first = second = head
        # for i in range(n):
        #     first = first.next
        # # case: delete the first node
        # if first is None:
        #     return head.next
        # # now first has traversed to position n, length-n to go.
        # # first, second traverse together to get to the right position
        # while first.next is not None:
        #     first = first.next
        #     second = second.next
        # # delete the node
        # second.next = second.next.next
        # return head

        # two pointers with a dummy head
        dummy_head = ListNode(-1)
        dummy_head.next = head
        pt1 = pt2 = dummy_head
        for _ in range(n):
            pt1 = pt1.next
        # edge case: delete the first node (nth from the last)
        if not pt1.next:
            return head.next
        while pt1.next:
            pt1 = pt1.next
            pt2 = pt2.next
        pt2.next = pt2.next.next
        return head
        
            
# @lc code=end

