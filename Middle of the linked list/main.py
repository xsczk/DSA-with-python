"""
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

Constraints:
- The number of nodes in the list is in the range [1, 100].
- 1 <= Node.val <= 100
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Floy's cycle detection
# time complexity: O(n)
# space complexity: O(1)
class Solution:
    def middle_node(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow