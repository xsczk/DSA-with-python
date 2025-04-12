"""Given the root of a binary tree and an integer targetSum,
return all root-to-leaf paths where the sum of the node values in the path equals targetSum.
Each path should be returned as a list of the node values, not node references.

A root-to-leaf path is a path starting from the root and ending at any leaf node.
A leaf is a node with no children."""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def path_sum(self, root: Optional[TreeNode], target_sum: int) -> list[list[int]]:
        ans = []
        if not root: return ans

        # backtracking
        def find_path(node: TreeNode, path: list[int], remaining_sum: int):
            if not node: return
            # add current node value to path
            path.append(node.val)
            # base case
            # if we are currently at a leaf node and current node value is equal to the remaining sum
            if not node.left and not node.right and remaining_sum == node.val:
                ans.append(path[:])
            # recursive call with left children and right children node
            else:
                find_path(node=node.left, path=path, remaining_sum=remaining_sum - node.val)
                find_path(node=node.right, path=path, remaining_sum=remaining_sum - node.val)
            # backtrack
            path.pop()

        find_path(node=root, path=[], remaining_sum=target_sum)
        return ans
