"""Given the head of a linked list and an integer val,
remove all the nodes of the linked list that has Node.val == val, and return the new head."""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def remove_elements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        cur = head
        # create dummy node
        new_list = ListNode()
        # point the new list to the head of the original list
        new_list.next = head
        prev = new_list
        while cur:
            if cur.val == val:
                prev.next = cur.next
            else:
                # move prev forward only if current node is not removed
                prev = cur
            cur = cur.next
        # dummy.next is the new head
        return new_list.next
