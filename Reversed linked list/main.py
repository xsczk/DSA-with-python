"""Given the head of a singly linked list, reverse the list,
and return the reversed list.

"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Time complexity: O(n)
# Space complexity: O(1)
class Solution:
    def reverse_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None
        while curr is not None:
            # save the next node to a temporary var
            temp = curr.next
            # reverse the next value of current to be the prev
            curr.next = prev
            # assign prev to current and current to temp for the next loop
            prev = curr
            curr = temp
        # prev now is the head of the reverse linked list
        return prev


