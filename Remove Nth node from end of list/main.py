"""Given the head of a linked list, remove the nth node
from the end of the list and return its head.

"""
from typing import Optional

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Time complexity: O(2 * length - n)
    # Space complexity: O(1)
    def remove_nth_from_end(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        length = 0
        while temp:
            length += 1
            temp = temp.next
        # if length equal to n, remove the head of the linked list
        if length == n: return head.next
        length -= (n + 1)
        before_removed_node = head
        # reverse the linked list till the node right before the removed node
        while length > 0:
            length -= 1
            before_removed_node = before_removed_node.next
        # remove the node at the nth of linked list
        before_removed_node.next = before_removed_node.next.next
        return head

    # Time complexity: O(length)
    # Space complexity: O(1)
    def remove_nth_node_from_end(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ans = ListNode()
        ans.next = head
        first = ans
        second = ans
        for i in range(1, n + 2):
            first = first.next
        # at the end of this loop, while first point to None,
        # second will be at the position right before the removed node
        while first is not None:
            first = first.next
            second = second.next
        second.next = second.next.next
        return ans.next