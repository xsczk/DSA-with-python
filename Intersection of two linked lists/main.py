"""Given the heads of two singly linked-lists headA and headB,
return the node at which the two lists intersect.
If the two linked lists have no intersection at all, return null.

The test cases are generated such that there are no cycles anywhere in the entire linked structure.

Note that the linked lists must retain their original structure after the function returns.

Custom Judge:
- The inputs to the judge are given as follows (your program is not given these inputs):
- intersectVal - The value of the node where the intersection occurs. This is 0 if there is no intersected node.
- listA - The first linked list.
- listB - The second linked list.
- skipA - The number of nodes to skip ahead in listA (starting from the head)
to get to the intersected node.
- skipB - The number of nodes to skip ahead in listB (starting from the head)
to get to the intersected node.
- The judge will then create the linked structure based on these inputs and pass the two heads,
headA and headB to your program. If you correctly return the intersected node,
then your solution will be accepted.

Constraints:
- The number of nodes of listA is in the m.
- The number of nodes of listB is in the n.
- 1 <= m, n <= 3 * 10^4
- 1 <= Node.val <= 10^5
- 0 <= skipA <= m
- 0 <= skipB <= n
- intersectVal is 0 if listA and listB do not intersect.
- intersectVal == listA[skipA] == listB[skipB] if listA and listB intersect.

"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # two pointers
    # Time complexity: O(m + n) where m and n are the length of the listA and listB respectively
    # Space complexity: O(1)
    def get_intersection_node(self, head_a: ListNode, head_b: ListNode) -> Optional[ListNode]:
        if not head_a or not head_b:
            return None
        a, b = head_a, head_b
        while a != b:
            # when a pointer reaches the end of its list, move it to the head of the other list.
            # if the lists intersect, the pointers will meet at the intersection node,
            # or both pointers will be None otherwise.
            a = a.next if a else head_b
            b = b.next if b else head_a
        return a

    # hash table
    # Time complexity: O(m + n)
    # Space complexity: O(n)
    def get_intersection_node_2(self, head_a: ListNode, head_b: ListNode) -> Optional[ListNode]:
        if not head_a or not head_b:
            return None
        map = {}
        cur = head_a
        # assign every node address to map with truthy value
        while cur:
            map[cur] = True
            cur = cur.next
        cur = head_b
        while cur:
            # check if node address in listB is represented in the map,
            # if satisfied, return this node otherwise return null
            if cur in map:
                return cur
            cur = cur.next
        return None
