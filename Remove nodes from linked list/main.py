"""You are given the head of a linked list.

Remove every node which has a node with a greater value anywhere to the right side of it.

Return the head of the modified linked list."""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def remove_nodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse_linked_list(root: Optional[ListNode]) -> Optional[ListNode]:
            """reverse the input linked list and return the reversed list"""
            prev, cur = None, root
            while cur is not None:
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp
            return prev

        reversed_list = reverse_linked_list(head)
        # traverse the reversed list and append the current max node's value
        cur, prev = reversed_list, None
        max = float('-Inf')
        while cur:
            if cur.val < max:
                # remove current node and persist prev node
                prev.next = cur.next
            else:
                # update current max value
                max = cur.val
                prev = cur
            cur = cur.next
        new_head = reverse_linked_list(reversed_list)
        return new_head
