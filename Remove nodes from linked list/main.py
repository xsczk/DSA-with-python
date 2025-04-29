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
    # using stack to keep track the maximum value
    # Time complexity: O(n)
    # Space complexity: O(n) due to stack size
    def remove_nodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 5 -> 2 -> 13 -> 3 -> 8
        stack = []
        cur = head
        while cur is not None:
            stack.append(cur)
            cur = cur.next
        # cur will now contain each node at reverse order
        cur = stack.pop()
        # initialize maximum value
        maximum = cur.val
        result_list = ListNode(maximum)
        while stack:
            cur = stack.pop()
            if maximum <= cur.val:
                # append current node to current result_list
                cur.next = result_list
                result_list = cur
            maximum = max(maximum, cur.val)
        return result_list



    # reverse the linked list twice
    # Time complexity: O(n)
    # Space complexity: O(1)
    def remove_nodes_2(self, head: Optional[ListNode]) -> Optional[ListNode]:
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

    # recursion
    # Time complexity: O(n)
    # Space complexity: O(n) due to recursion stack
    def remove_nodes_3(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # base case: reached end of the list
        if not head or not head.next: return head
        # recursive call to head.next
        next_node = self.remove_nodes_3(head.next)
        # If the next node has greater value than head, delete the head
        # Return next node, which removes the current head and
        # makes next the new head
        if head.val < next_node.val:
            return next_node
        # keep the head
        head.next = next_node
        return head



