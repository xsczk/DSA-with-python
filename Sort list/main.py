"""Given the head of a linked list, return the list after sorting it
in ascending order."""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # merge sort and two pointers technique to split the linked list into two halves
    def merge_two_sorted_list(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """helper method to merge two sorted linked list and return new sorted linked list"""
        dummy = ListNode()
        head = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                head.next = l1
                l1 = l1.next
            else:
                head.next = l2
                l2 = l2.next
            head = head.next
        # connect head to the remaining list
        head.next = l1 or l2
        return dummy.next

    # Time complexity: O(n*log n)
    # Space complexity: O(log n) due to recursion stack
    def sort_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # base case
        if not head or not head.next: return head
        slow, fast, prev = head, head, None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        # split the linked list in to two halves: head and slow is the new head of two linked list
        prev.next = None
        # recursive call to head and slow
        left = self.sort_list(head)
        right = self.sort_list(slow)
        return self.merge_two_sorted_list(left, right)

    # modify the linked list directly
    # Time complexity: O(n*log n)
    # Space complexity: O(n) due to values list
    def sort_list_2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        values = []
        cur = head
        while cur:
            values.append(cur.val)
            cur = cur.next
        # values now stored all node's value
        cur = head
        values.sort()
        for i in range(len(values)):
            cur.val = values[i]
            cur = cur.next
        return head