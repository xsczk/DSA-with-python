"""Given the head of a linked list, rotate the list to the right by k places."""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # Two-Pointer Traversal + Modulo Arithmetic
    # Time complexity: O(n)
    # Space complexity: O(1)
    def rotate_right(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        # compute the length and get the tail node
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1
        # reduce unnecessary rotations with modulo
        k = k % length
        if k == 0:
            return head
        # find the new tail: (length - k - 1)th node
        new_tail = head
        for _ in range(length - k - 1):
            new_tail = new_tail.next
        # rewire pointers
        new_head = new_tail.next
        new_tail.next = None
        tail.next = head

        return new_head
