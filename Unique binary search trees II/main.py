"""Given an integer n, return all the structurally unique BST's (binary search trees),
which has exactly n nodes of unique values from 1 to n. Return the answer in any order."""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generate_tree(self, n: int) -> list[Optional[TreeNode]]:
        memo = {}

        def all_possible_BST(start: int, end: int):
            res = []
            # base case: if start > end, we have no values in our range,
            # and thus we will return null (an empty tree).
            if start > end:
                res.append(None)
                return res
            if (start, end) in memo: return memo[(start, end)]
            # Iterate through all values from start to end
            # to construct left and right subtree recursively.
            for root_val in range(start, end + 1):
                # since this is a binary search tree: all values in the left subtree are smaller
                # and all values in the right subtree are greater.
                # if root_val is considered as a root node
                # => left subtrees will have root_val - 1 nodes from 1 -> root_val - 1
                # right subtrees will have end - root_val nodes from root_val + 1 -> end
                left_sub_trees = all_possible_BST(start, root_val - 1)
                right_sub_trees = all_possible_BST(root_val + 1, end)
                # Loop through all left and right subtrees
                # and connect them to ith root.
                for left in left_sub_trees:
                    for right in right_sub_trees:
                        root = TreeNode(val=root_val, left=left, right=right)
                        res.append(root)
            # assign res to memo for skip recalculating sub problem again
            memo[(start, end)] = res
            return res

        return all_possible_BST(start=1, end=n)
