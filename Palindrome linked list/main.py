"""Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def is_palindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next: return True
        cur = head
        stack = []
        while cur:
            stack.append(cur.val)
            cur = cur.next
        if stack == stack[::-1]: return True
        return False

