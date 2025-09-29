"""
You are given two non-empty linked lists representing two non-negative integers.
The most significant digit comes first and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:
Input: l1 = [7,2,4,3], l2 = [5,6,4]
Output: [7,8,0,7]

Example 2:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [8,0,7]

Example 3:
Input: l1 = [0], l2 = [0]
Output: [0]

Constraints:
- The number of nodes in each linked list is in the range [1, 100].
- 0 <= Node.val <= 9
- It is guaranteed that the list represents a number that does not have leading zeros.
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def add_two_numbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> \
            Optional[ListNode]:

        def add_to_stack(linked_list: Optional[ListNode]) -> list[int]:
            stack = []
            while linked_list:
                stack.append(linked_list.val)
                linked_list = linked_list.next
            return stack

        st1 = add_to_stack(l1)
        st2 = add_to_stack(l2)
        total, carry = 0, 0
        res = ListNode()

        while st1 or st2:
            if st1:
                total += st1.pop()
            if st2:
                total += st2.pop()
            res.val = total % 10
            # if total of two digits >= 10 => carry = 1; 0 otherwise
            carry = total // 10
            # save the carry; in 99 + 1 = 100, the carry produces the new leading digit 1.
            head = ListNode(carry)
            head.next = res
            res = head
            # save the carry for the next operator
            total = carry
        return res.next if carry == 0 else res
