"""
Given the root of a binary search tree and an integer k,
return true if there exist two elements in the BST such that their sum is equal to k,
or false otherwise.

Constraints:
- The number of nodes in the tree is in the range [1, 104].
- -10^4 <= Node.val <= 10^4
- root is guaranteed to be a valid binary search tree.
- -10^5 <= k <= 10^5
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def find_target(self, root: Optional[TreeNode], k: int) -> bool:
        visited = set()
        ans = [False]

        def dfs(node: Optional[TreeNode]) -> None:
            if not node or ans[0]:
                return
            if node.val in visited:
                ans[0] = True
                return
            visited.add(k - node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ans[0]
