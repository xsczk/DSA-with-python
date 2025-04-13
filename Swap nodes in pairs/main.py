"""Given a linked list, swap every two adjacent nodes and return its head.
You must solve the problem without modifying the values in the list's nodes
(i.e., only nodes themselves may be changed.)

"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swap_pairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def swap_head(head: Optional[ListNode]) -> Optional[ListNode]:
            if head is None or head.next is None: return head
            first = head
            second = head.next
            # assign first node to the next of second node
            first.next = second.next
            # swap first and second so that first node
            # will be the previous node of second node
            second.next = first
            # call recursive function on first.next to calc the next two node
            first.next = swap_head(first.next)
            # return new head
            return second
        return swap_head(head)