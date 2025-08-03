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
