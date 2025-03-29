"""You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

"""
from typing import Optional


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Time complexity: O()
# Space complexity: O(1)
class Solution:
    def merge_k_lists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0: return None
        i, j = 0, len(lists) - 1
        while j > 0:
            lists[i] = self.merge_two_lists(l1=lists[i], l2=lists[j])
            i += 1
            j -= 1
            if i >= j: i = 0
        return lists[i]

    def merge_two_lists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr = ListNode()
        ans = curr
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        while l1:
            curr.next = l1
            l1 = l1.next
            curr = curr.next
        while l2:
            curr.next = l2
            l2 = l2.next
            curr = curr.next
        return ans.next

    def merge_two_list_recursion(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val < l2.val:
            l1.next = self.merge_two_list_recursion(l1.next, l2)
            return l1
        else:
            l2.next = self.merge_two_list_recursion(l1, l2.next)
            return l2
