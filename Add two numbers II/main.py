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
        carry, sum_st = 0, []

        def calc_carry(digit_sum: int) -> int:
            return 1 if digit_sum >= 10 else 0

        while st1 and st2:
            most_left_digit1 = st1.pop()
            most_left_digit2 = st2.pop()
            digit_sum = most_left_digit1 + most_left_digit2 + carry
            sum_st.append(digit_sum % 10)
            carry = calc_carry(digit_sum)
        while st1:
            digit = st1.pop()
            digit_sum = digit + carry
            sum_st.append(digit_sum % 10)
            carry = calc_carry(digit_sum)
        while st2:
            digit = st2.pop()
            digit_sum = digit + carry
            sum_st.append(digit_sum % 10)
            carry = calc_carry(digit_sum)
        if carry:
            sum_st.append(carry)
        res = ListNode()
        dummy = res
        while sum_st:
            dummy.next = ListNode(sum_st.pop())
            dummy = dummy.next
        return res.next
