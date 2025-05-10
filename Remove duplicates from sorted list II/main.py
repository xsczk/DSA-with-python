"""Given the head of a sorted linked list, delete all nodes that have duplicate numbers,
leaving only distinct numbers from the original list. Return the linked list sorted as well."""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    # two pointers
    # Time complexity: O(n) - each node is visited once
    # Space complexity: O(1) - we mutate the head directly and did not use extra space
    def delete_duplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        # create a dummy node named prev to keep track the last node before the duplicate sequence
        prev, cur = ListNode(), head
        dummy = prev
        # connect dummy to original linked list
        prev.next = head
        while cur:
            is_duplicate = False
            # check if the current value is equal to next value.
            # If so, keep the prev and move cur forward
            while cur.next and cur.val == cur.next.val:
                is_duplicate = True
                cur = cur.next
            # if duplicate sequence is found, connect prev to cur.next
            # (cur is the last node of the sequence)
            if is_duplicate:
                prev.next = cur.next
            # move prev and cur forward
            else:
                prev = cur
            cur = cur.next
        return dummy.next