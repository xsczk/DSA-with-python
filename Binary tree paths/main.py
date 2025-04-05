"""Given the root of a binary tree,
return all root-to-leaf paths in any order.

A leaf is a node with no children."""
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # stack + dfs
    def binary_tree_paths(self, root: Optional[TreeNode]) -> list[str]:
        if not root: return []
        ans, stack = [], [(root, '')]
        while stack:
            node, path = stack.pop()
            if not node.left and not node.right:
                ans.append(path + str(node.val))
            if node.left:
                stack.append((node.left, path + f'{node.val}->'))
            if node.right:
                stack.append((node.right, path + f'{node.val}->'))
        return ans

    # queue + bfs
    def binary_tree_paths_2(self, root: Optional[TreeNode]) -> list[str]:
        if not root: return []
        ans, queue = [], deque([(root, "")])
        while queue:
            node, path = queue.popleft()
            if not node.left and not node.right:
                ans.append(path + str(node.val))
            if node.left:
                queue.append((node.left, path + f'{node.val}->'))
            if node.right:
                queue.append((node.right, path + f'{node.val}->'))
        return ans

    # recursive + dfs
    def binary_tree_paths_3(self, root: Optional[TreeNode]) -> list[str]:
        if not root: return []

        def dfs(node: TreeNode, path=''):
            if not node.left and not node.right:
                path += str(node.val)
                ans.append(path)
            if node.left:
                dfs(node.left, path + f'{node.val}->')
            if node.right:
                dfs(node.right, path + f'{node.val}->')

        ans = []
        dfs(root)
        return ans

# [1,2,3,null,5]
