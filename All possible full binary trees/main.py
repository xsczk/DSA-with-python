"""Given an integer n, return a list of all possible full binary trees with n nodes.
Each node of each tree in the answer must have Node.val == 0.

Each element of the answer is the root node of one possible tree.
You may return the final list of trees in any order.

A full binary tree is a binary tree where each node has exactly 0 or 2 children."""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # recursion with memoization
    def __init__(self):
        self.memo = {}
    def all_possible_FBT(self, n: int) -> list[Optional[TreeNode]]:
        # base case: n % 2 == 0, return directly [] because we cannot form any full binary tree
        # with even number of nodes.
        if n % 2 == 0: return []
        # base case: n == 1, return a list with a single tree node has no children
        if n == 1: return [TreeNode()]
        # return directly if we found same sub problem result in previous callstack
        if n in self.memo: return self.memo[n]
        res = []
        # step == 2 as we know we can only form full binary tree if number of nodes is odd
        for i in range(1, n, 2):
            # recursive call with left and right subtree
            left_list = self.all_possible_FBT(i)
            right_list = self.all_possible_FBT(n - 1 - i)
            # combine them for all possible full binary trees
            for left in left_list:
                for right in right_list:
                    # build the binary tree
                    root = TreeNode(val=0, left=left, right=right)
                    res.append(root)
        self.memo[n] = res
        return res


solution = Solution()
all_bin_trees = solution.all_possible_FBT(7)
print(all_bin_trees)