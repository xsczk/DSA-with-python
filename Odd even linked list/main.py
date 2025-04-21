"""Given the head of a singly linked list, group all the nodes with odd indices together
followed by the nodes with even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

You must solve the problem in O(1) extra space complexity and O(n) time complexity.

"""
from typing import Optional


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Time complexity: O(n)
# Space complexity: O(1)
class Solution:
    def odd_even_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None: return head
        odd = head
        even = odd.next
        even_list = even
        # event.next is valid means that there is still odd node to traverse.
        while even and even.next:
            # the next odd will be the even.next and vice versa
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        # after the loop, connect the odd.next to the head of the even which is even_list
        odd.next = even_list
        return head
