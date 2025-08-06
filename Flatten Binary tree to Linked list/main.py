"""
Given the root of a binary tree, flatten the tree into a "linked list":

- The "linked list" should use the same TreeNode class
where the right child pointer points to the next node in the list
and the left child pointer is always null.
- The "linked list" should be in the same order as a pre-order traversal of the binary tree.

Constraints:
- The number of nodes in the tree is in the range [0, 2000].
- -100 <= Node.val <= 100
"""

"""
                1
              /   \
             2     5     =>  1 -> 2 -> 3 -> 4 -> 5 -> 6
            / \     \
           3   4     6
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.head = None

    def pre_order_traversal(self, node: Optional[TreeNode],
                            stack: list[Optional[TreeNode]]) -> None:
        if node is not None:
            self.pre_order_traversal(node.right, stack)
            self.pre_order_traversal(node.left, stack)
            stack.append(node)

    # stack, recursion
    # time complexity: O(n)
    # space complexity: O(n)
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        stack: list[Optional[TreeNode]] = []
        if root:
            self.pre_order_traversal(root, stack)
        while stack:
            head = stack.pop()
            # left child pointer is always null
            head.left = None
            # right child pointer points to the next node in the list
            head.right = None if len(stack) - 1 < 0 else stack[-1]

    # recursion
    # time complexity: O(n)
    # space complexity: O(1)
    def pre_order_helper(self, node: Optional[TreeNode]) -> None:
        if node is not None:
            self.pre_order_helper(node.right)
            self.pre_order_helper(node.left)
            # left child pointer is always null
            node.left = None
            # current right child will be the head
            # which is assigned to the node of the next recur function in the callstack
            node.right = self.head
            self.head = node

    def flatten_2(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.pre_order_helper(root)
