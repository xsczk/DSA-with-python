"""You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list.
The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list."""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Time complexity: O(n)
# Space complexity: O(1)
class Solution:
    def merge_two_lists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr = ListNode()
        ans = curr
        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        while list1:
            curr.next = list1
            list1 = list1.next
            curr = curr.next
        while list2:
            curr.next = list2
            list2 = list2.next
            curr = curr.next
        return ans.next


