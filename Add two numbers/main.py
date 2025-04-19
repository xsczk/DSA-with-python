"""You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains
a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero,
except the number 0 itself.

"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # two pointers approach
    def add_two_numbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode()
        carry = 0
        p = ans
        while l1 or l2:
            sum = carry
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
            carry = sum // 10
            p.next = ListNode(sum % 10)
            p = p.next
        # check if carry still is 1 => add 1 to answer
        if carry == 1:
            p.next = ListNode(carry)
        return ans.next

    # recursion
    def add_two_numbers_2(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # calc the number formed by linked list
        # ex: 2 -> 4 -> 3: 342
        def linkedlist_to_int(l: Optional[ListNode]):
            if l.next is None: return l.val
            return l.val + linkedlist_to_int(l.next) * 10

        num1 = linkedlist_to_int(l1)
        num2 = linkedlist_to_int(l2)

        # convert int to linked list
        # ex: 807: 7 -> 0 -> 8
        def int_to_linkedlist(num: int) -> Optional[ListNode]:
            if num < 10: return ListNode(val=num)
            units = num % 10
            return ListNode(val=units, next=int_to_linkedlist(num // 10))

        return int_to_linkedlist(num1 + num2)
