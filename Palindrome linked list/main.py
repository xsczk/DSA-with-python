"""Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n) due to stack value
    def is_palindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next: return True
        cur = head
        stack = []
        while cur:
            stack.append(cur.val)
            cur = cur.next
        if stack == stack[::-1]: return True
        return False

    # Time complexity: O(n)
    # Space complexity: O(1)
    def is_palindrome_2(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next: return True
        # using floyd cycle detection's algorithm to find the middle of the linked list
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # reverse the second half linked list
        # 1 -> 2 -> 3 -> 4 => 4 -> 3 -> 2 -> 1
        cur, prev = slow.next, None
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        fast = head
        # compare each node of prev and fast
        # prev now is the reversed version of second half linked list
        while prev:
            if prev.val != fast.val: return False
            prev = prev.next
            fast = fast.next

        return True




