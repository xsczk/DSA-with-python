"""Given the head of a linked list, return the node where the cycle begins.
If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list
that can be reached again by continuously following the next pointer.
Internally, pos is used to denote the index of the node that
tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle.
Note that pos is not passed as a parameter.

Do not modify the linked list."""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # two pointers with Floyd’s cycle finding algorithm
    # Time complexity: O(n)
    # Space complexity: O(1)
    def detect_cycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # define two pointer, slow will traverse through the linked list with one step at a time
        # while fast traverses with two steps
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            # if fast meets slow at some point, that means the linked list is a cycle
            if slow == fast:
                break
        # if fast is None, that means linked list is not a cycle, return None directly
        if not fast or not fast.next: return None
        # assign slow to head again, now looping until slow meets fast again but both traverse
        # through the linked list with one step at a time. the slow pointer finally points to
        # the node where the cycle begins
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow