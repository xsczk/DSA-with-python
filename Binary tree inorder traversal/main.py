"""
Given the root of a binary tree, return the inorder traversal of its nodes' values.

Constraints:
- The number of nodes in the tree is in the range [0, 100].
- -100 <= Node.val <= 100
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def helper(self, node: Optional[TreeNode], result: list[int]) -> None:
        if node is not None:
            # traverse every left subtree nodes
            self.helper(node.left, result)
            # append the current parent node's value
            result.append(node.val)
            # traverse the right subtree nodes
            self.helper(node.right, result)

    # recursive
    # time complexity: O(n)
    # space complexity: O(n)
    def inorder_traversal(self, root: Optional[TreeNode]) -> list[int]:
        res = []
        self.helper(root, res)
        return res

    # using stack based on the logic of recursive approach
    # time complexity: O(n)
    # space complexity: O(n)
    def inorder_traversal_stack(self, root: Optional[TreeNode]) -> list[int]:
        res = []
        stack = []
        curr = root
        while curr or stack:
            # traverse all the left subtree nodes
            while curr:
                stack.append(curr)
                curr = curr.left
            # if not any left nodes found, push the recent node's value to res
            curr = stack.pop()
            res.append(curr.val)
            # start traversing right subtree nodes
            curr = curr.right
        return res
