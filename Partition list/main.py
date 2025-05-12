"""Given the head of a linked list and a value x, partition it such that all nodes less than x
come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions."""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # create two dummy lists, one stores nodes whose values are smaller than x
        # the other stores values bigger than x
        less_list = ListNode()
        greater_list = ListNode()
        cur, less, greater = head, less_list, greater_list
        # push each node in head to corresponding list
        while cur:
            if cur.val < x:
                less.next = cur
                less = less.next
            else:
                greater.next = cur
                greater = greater.next
            cur = cur.next
        # connect less_list and greater_list
        greater.next = None
        less.next = greater_list.next
        return less_list.next
