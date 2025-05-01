"""Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes
along the longest path from the root node down to the farthest leaf node.

"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def max_depth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        def dfs(node: Optional[TreeNode]) -> int:
            # base case: return node count for current leaf node
            if not node.left and not node.right:
                return 1
            # initialize current node count for left and right
            left, right = 1, 1
            if node.left:
                left += dfs(node.left)
            if node.right:
                right += dfs(node.right)
            # return greater depth
            return max(left, right)

        return dfs(root)
