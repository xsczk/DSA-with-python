"""You are given the root of a binary search tree (BST) and an integer val.

Find the node in the BST that the node's value equals val
and return the subtree rooted with that node. If such a node does not exist,
return null."""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def search_BST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def dfs(node: Optional[TreeNode]):
            # return null if node is None,
            # or it is a leaf node and its value is not equal to val
            if not node or (not node.right and not node.left and node.val != val): return None
            # since root is a binary search tree
            # if current value is bigger than val => recursive call with node.left
            # else call with node.right
            if node.val > val:
                return dfs(node.left)
            elif node.val < val:
                return dfs(node.right)
            return node

        return dfs(root)
