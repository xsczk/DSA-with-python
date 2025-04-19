"""You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def reorder_list(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # use slow and fast to find the middle of the linked list
        slow, fast = head, head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        # reverse the second half of the linked list
        cur = slow.next
        # this will be the head of reversed list after while loop
        reversed_head: Optional[ListNode] = None
        while cur:
            temp = cur.next
            cur.next = reversed_head
            reversed_head = cur
            cur = temp

        # make the end of first half linked list is None
        slow.next = None
        # merge the first half list with the reversed list
        first = head
        second = reversed_head
        while second:
            temp_1, temp_2 = first.next, second.next
            first.next, second.next = second, temp_1
            first, second = temp_1, temp_2






