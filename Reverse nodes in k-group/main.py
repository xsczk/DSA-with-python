"""Given the head of a linked list, reverse the nodes of the list k at a time,
and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list.
If the number of nodes is not a multiple of k then left-out nodes,
in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed."""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # Time complexity: O(n) as we traverse through the initial linked list
    # Space complexity: O(1) no extra space needed since we just use few variables
    def reverse_list(self, head: Optional[ListNode], k: int) -> [Optional[ListNode], Optional[ListNode]]:
        if not head: return None
        cur, prev = head, None
        for _ in range(k):
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        # return the reversed head and the next node after k elements
        return prev, cur

    def reverse_k_group(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        traverse = dummy
        while traverse:
            tracker = traverse
            # check if there are k nodes enough to reverse
            for _ in range(k):
                tracker = tracker.next
                # if there are not enough nodes, return result
                if not tracker: return dummy.next
            # reverse k nodes
            # prev is new reversed head of group of k nodes, cur is the next node after k nodes
            prev, cur = self.reverse_list(traverse.next, k)
            last_node_of_reversed_list = traverse.next
            # connect last node of reversed list to remaining nodes of the initial list
            last_node_of_reversed_list.next = cur
            # connect dummy head to new reversed list's head
            traverse.next = prev
            # reassign traverse to continue looping
            traverse = last_node_of_reversed_list
        return dummy.next
