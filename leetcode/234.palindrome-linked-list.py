#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # O(n) time and O(n) space
        if head is None or head.next is None:
            return True
        pointer = pointer2 = head
        lllen = 0
        while pointer is not None:
            lllen += 1
            pointer = pointer.next
        stack = []
        for _ in range(lllen//2):
            stack.append(pointer2.val)
            pointer2 = pointer2.next
        if lllen%2 == 1:
            pointer2 = pointer2.next
        for _ in range(lllen//2):
            if pointer2.val != stack.pop():
                return False
            pointer2 = pointer2.next
        return True

        # how to get O(1) space?
        # find the middle node, and reverse the latter and compare
        
# @lc code=end

